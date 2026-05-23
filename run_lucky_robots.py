#!/usr/bin/env python3
"""
Moving Day Simulator - Lucky Robots SDK Setup
Demonstrates starting a 3D robotic simulation session loading our custom apartment layout.
"""

import sys
import os

try:
    from luckyrobots import Session
except ImportError:
    print("Error: The 'luckyrobots' package is not installed.")
    print("Please install it first using uv:")
    print("  uv pip install luckyrobots")
    sys.exit(1)

def main():
    scene_path = "apartment_3d.xml"
    if not os.path.exists(scene_path):
        print(f"Error: {scene_path} not found. Run ./compile_3d_scene.py first.")
        sys.exit(1)

    print("=====================================================================")
    print("                LUCKY ROBOTS SDK SIMULATOR SETUP")
    print("=====================================================================")
    print(f"Loading custom 3D scene: {scene_path}")
    print("Spawning robot agent: Unitree Go2 (quadruped moving assistant)")
    print("---------------------------------------------------------------------")

    # Check if LuckyEngine executable is specified in the environment variables
    engine_path = os.environ.get("LUCKYENGINE_PATH") or os.environ.get("LUCKYENGINE_HOME")
    if not engine_path:
        print("WARNING: 'LUCKYENGINE_PATH' environment variable is not set.")
        print("Lucky Robots SDK requires the LuckyEngine binary to run physics/rendering.")
        print("You can download the LuckyEngine binary for Linux from:")
        print("  https://github.com/luckyrobots/luckyrobots#installation")
        print("\nOnce downloaded, set the path before running:")
        print("  export LUCKYENGINE_PATH=/path/to/luckyengine-binary")
        print("=====================================================================\n")

    try:
        # Launching a managed session with the SDK
        with Session() as session:
            # We pass our compiled XML as the scene, select the robot, and specify the task
            session.start(
                scene=scene_path,
                robot="unitreego2",
                task="navigation"
            )
            print("Session started successfully!")
            
            # Reset environment and get initial observations
            obs = session.reset()
            print("Environment reset successful.")
            
            # Simulate a few steps sending neutral actions (stationary)
            print("Simulating 100 control steps...")
            for step in range(100):
                # Unitree Go2 has 12 joints (3 per leg)
                neutral_actions = [0.0] * 12
                obs = session.step(actions=neutral_actions)
                
                if step % 20 == 0:
                    print(f"  Step {step:02d}: Simulated successfully.")
                    
            print("\nRobotic simulation walk finished successfully.")
            
    except Exception as e:
        print(f"\nFailed to launch session: {e}")
        print("This is expected if LuckyEngine binary is missing or not running in the background.")
        print("To test the layout physics visually without the SDK engine, run:")
        print("  uv run --with mujoco python3 -m mujoco.viewer --mjcf=apartment_3d.xml")

if __name__ == "__main__":
    main()
