#!/usr/bin/env python3
"""
Moving Day Simulator - Lucky Robots SDK Simulation
Launches the custom 3D apartment floorplan and coordinates a basic control loop.
"""

import sys
import os
import asyncio
import logging
import numpy as np

try:
    from luckyrobots import (
        Node,
        LuckyRobots,
        Reset,
        Step,
        run_coroutine,
    )
except ImportError:
    print("Error: The 'luckyrobots' package is not installed.")
    print("Please install it first using uv:")
    print("  uv pip install luckyrobots")
    sys.exit(1)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("moving_simulator")


class MovingAssistantController(Node):
    """Custom control node for our robotic moving assistant"""

    def __init__(self, name: str = "assistant_controller", robot: str = "stretch_v1", host: str = "localhost", port: int = 3000):
        super().__init__(name, namespace="", host=host, port=port)
        self.robot = robot
        self.robot_config = LuckyRobots.get_robot_config(robot)
        self.loop_running = False
        logger.info(f"Initialized MovingAssistantController for {robot}")

    async def _setup_async(self) -> None:
        """Initialize the client services to communicate with the engine"""
        self.reset_client = self.create_client(Reset, "/reset")
        self.step_client = self.create_client(Step, "/step")

    def start_control_loop(self, rate_hz: float = 10.0) -> None:
        """Launch the asynchronous control loop using the SDK event runner"""
        self.loop_running = True
        run_coroutine(self.run_loop(rate_hz))

    async def run_loop(self, rate_hz: float) -> None:
        """Run the main simulation loop"""
        period = 1.0 / rate_hz
        logger.info("Waiting for simulation engine to warm up...")
        await asyncio.sleep(2.0)

        # Reset the environment to place objects and helper
        logger.info("Sending reset request to place robot and objects...")
        try:
            response = await self.reset_client.call(Reset.Request())
            logger.info("Scene reset successfully!")
        except Exception as e:
            logger.error(f"Failed to reset environment: {e}")
            self.loop_running = False
            return

        # Simple walk/moving loop (neutral actions)
        limits = self.robot_config["action_space"]["actuator_limits"]
        action_dim = len(limits)
        logger.info(
            f"Starting control loop at {rate_hz} Hz (Action dimension: {action_dim})"
        )

        step_idx = 0
        try:
            while self.loop_running:
                # Send neutral actuator commands (0.0 values) to let robot settle
                actuator_values = np.zeros(action_dim)
                response = await self.step_client.call(
                    Step.Request(actuator_values=actuator_values)
                )

                if step_idx % 20 == 0:
                    logger.info(f"Simulated step {step_idx}...")

                step_idx += 1
                await asyncio.sleep(period)
        except Exception as e:
            logger.error(f"Error during control step: {e}")
        finally:
            self.loop_running = False
            logger.info("Simulation control loop terminated.")

    def stop_control_loop(self) -> None:
        self.loop_running = False


def main():
    scene_path = "apartment_3d.xml"
    if not os.path.exists(scene_path):
        print(f"Error: {scene_path} not found. Run ./compile_3d_scene.py first.")
        sys.exit(1)

    # Locate the compiled LuckyEngine binary
    engine_path = os.environ.get("LUCKYENGINE_PATH") or os.environ.get(
        "LUCKYENGINE_HOME"
    )
    if not engine_path:
        print("=====================================================================")
        print("WARNING: 'LUCKYENGINE_PATH' is not set.")
        print("Please point it to your extracted LuckyEngine directory, e.g.:")
        print(
            "  export LUCKYENGINE_PATH=/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64"
        )
        print("=====================================================================\n")

    # We use stretch_v1 (the mobile manipulator robot)
    robot_model = "stretch_v1"

    try:
        # 1. Initialize the main manager node
        luckyrobots = LuckyRobots()

        # 2. Initialize and register our custom controller node
        controller = MovingAssistantController(
            robot=robot_model,
            host=luckyrobots.host,
            port=luckyrobots.port
        )
        luckyrobots.register_node(controller)

        # 3. Start the simulation backend
        print("Starting simulation engine...")
        luckyrobots.start(
            scene=scene_path,
            robot=robot_model,
            task="navigation",
            game_path=engine_path,
        )

        # 4. Wait for client handshake connection
        print("Waiting for LuckyEngine gRPC client connection...")
        luckyrobots.wait_for_world_client(timeout=45.0)

        # 5. Start our controller's background loop
        controller.start_control_loop(rate_hz=10.0)

        # 6. Keep the node spinning to route messages
        luckyrobots.spin()

    except KeyboardInterrupt:
        print("\nShutdown requested by user. Terminating...")
    except Exception as e:
        print(f"\nSimulation process encountered an error: {e}")
    finally:
        if "controller" in locals():
            controller.stop_control_loop()
        print("Application exit.")


if __name__ == "__main__":
    main()
