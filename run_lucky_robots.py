#!/usr/bin/env python3
"""Moving Day Simulator runner for LuckyRobots SDK.

Supports both:
1) Launch + connect flow
2) Attach-to-running-engine flow (skip launch)
"""

import argparse
import shutil
import os
import socket
import sys
import time
import re

try:
    import numpy as np
except ImportError:
    print("Error: The 'numpy' package is not installed.")
    print("Please install dependencies first:")
    print("  make setup")
    sys.exit(1)

try:
    from luckyrobots import Session
    from luckyrobots.engine import launch_luckyengine
except ImportError:
    print("Error: The 'luckyrobots' package is not installed.")
    print("Please install dependencies first:")
    print("  make setup")
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", type=str, default="apartment_3d.xml")
    parser.add_argument("--robot", type=str, default="stretch_v1")
    parser.add_argument("--task", type=str, default="navigation")
    parser.add_argument("--rate-hz", type=float, default=10.0)
    parser.add_argument("--headless", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--skip-launch", action="store_true")
    parser.add_argument("--host", type=str, default="auto")
    parser.add_argument("--port", type=int, default=50051)
    parser.add_argument("--connect-timeout", type=float, default=120.0)
    parser.add_argument("--reset-timeout", type=float, default=120.0)
    parser.add_argument("--scan-ports", type=str, default="50051-50060")
    args = parser.parse_args()

    scene_path = args.scene
    if scene_path.endswith(".xml") and not os.path.isabs(scene_path):
        if not os.path.exists(scene_path):
            print(f"Error: {scene_path} not found. Run ./scripts/compile_3d_scene.py first.")
            sys.exit(1)
        scene_path = os.path.abspath(scene_path)

    default_engine_root = (
        "/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64"
    )
    engine_path = os.environ.get("LUCKYENGINE_PATH") or os.environ.get("LUCKYENGINE_HOME")
    if not engine_path and os.path.isdir(default_engine_root):
        engine_path = default_engine_root

    def parse_port_range(spec: str) -> list[int]:
        if "-" in spec:
            start_s, end_s = spec.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            if end < start:
                start, end = end, start
            return list(range(start, end + 1))
        return [int(spec)]

    def candidate_hosts() -> list[str]:
        if args.host != "auto":
            return [args.host]
        return ["127.0.0.1", "localhost", "172.24.160.1"]

    def candidate_ports() -> list[int]:
        ports = [args.port]
        for p in parse_port_range(args.scan_ports):
            if p not in ports:
                ports.append(p)
        return ports

    def tcp_is_open(host: str, port: int, timeout: float = 0.25) -> bool:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return True
        except OSError:
            return False

    def maybe_stage_xml_scene(local_xml: str, engine_root: str) -> str:
        """Copy xml to RobotSandbox assets and return scene key used for launch."""
        scene_key = os.path.splitext(os.path.basename(local_xml))[0]
        assets_dir = os.path.join(engine_root, "LuckyEditor", "RobotSandbox", "Assets")
        dst_xml = os.path.join(assets_dir, os.path.basename(local_xml))
        if os.path.isdir(assets_dir):
            shutil.copy2(local_xml, dst_xml)
            print(f"Staged XML scene to {dst_xml}")
            print(f"Launching by scene key '{scene_key}'")
            return scene_key
        print(f"Warning: RobotSandbox assets dir not found at {assets_dir}")
        print("Continuing with XML absolute path scene argument.")
        return local_xml

    period = 1.0 / args.rate_hz
    original_cwd = os.getcwd()
    session: Session | None = None

    try:
        engine_executable = None
        engine_root = None
        if engine_path:
            engine_executable = engine_path
            engine_root = (
                engine_path if os.path.isdir(engine_path) else os.path.dirname(os.path.dirname(engine_path))
            )
            if os.path.isdir(engine_path):
                engine_executable = os.path.join(engine_path, "bin", "LuckyEditor")
            engine_lib_dir = os.path.join(engine_root, "lib")
            if os.path.isdir(engine_lib_dir):
                existing_ld_path = os.environ.get("LD_LIBRARY_PATH", "")
                os.environ["LD_LIBRARY_PATH"] = (
                    f"{engine_lib_dir}:{existing_ld_path}" if existing_ld_path else engine_lib_dir
                )
            editor_dir = os.path.join(engine_root, "LuckyEditor")
            if os.path.isdir(editor_dir):
                os.chdir(editor_dir)
            # Ensure bundled .NET helper can be started even when IDE shells have a reduced PATH.
            if shutil.which("dotnet") is None:
                os.environ["PATH"] = f"/usr/bin:{os.environ.get('PATH', '')}"
            os.environ.setdefault("DOTNET_ROOT", "/usr/lib/dotnet")
            coral_managed = os.path.join(engine_root, "LuckyEditor", "DotNet", "Coral.Managed.dll")
            if not os.path.isfile(coral_managed):
                print(f"Warning: Coral.Managed.dll was not found at expected path: {coral_managed}")

        launch_scene = scene_path
        if (
            not args.skip_launch
            and engine_path
            and engine_root
            and isinstance(scene_path, str)
            and scene_path.endswith(".xml")
            and os.path.isabs(scene_path)
        ):
            launch_scene = maybe_stage_xml_scene(scene_path, engine_root)

        if not args.skip_launch:
            if not engine_path:
                print("WARNING: LUCKYENGINE_PATH is not set and launch mode was requested.")
                print("Set it, or use --skip-launch to attach to a running engine.")
                sys.exit(1)
            # Launch with the requested host/port baseline; then scan for actual listener.
            print("Starting simulation engine...")
            ok = launch_luckyengine(
                scene=launch_scene,
                robot=args.robot,
                task=args.task,
                executable_path=engine_executable,
                headless=args.headless,
            )
            if not ok:
                print("Engine launch failed before gRPC connection stage.")
                sys.exit(1)
        else:
            print("Skipping engine launch (--skip-launch).")

        hosts = candidate_hosts()
        ports = candidate_ports()
        total_candidates = len(hosts) * len(ports)
        print(f"Connecting to gRPC server (trying {total_candidates} host/port candidates)...")

        connected = False
        last_error: Exception | None = None
        deadline = time.time() + args.connect_timeout
        warned_editor_only = False
        while time.time() < deadline and not connected:
            for host in hosts:
                for port in ports:
                    # Quick TCP probe before full SDK connect avoids long hangs on dead endpoints.
                    if not tcp_is_open(host, port):
                        continue
                    try:
                        trial = Session(host=host, port=port)
                        trial.connect(timeout_s=max(2.0, min(args.connect_timeout, 15.0)), robot=args.robot)
                        session = trial
                        print(f"Connected to LuckyEngine gRPC at {host}:{port}")
                        connected = True
                        break
                    except Exception as exc:
                        last_error = exc
                if connected:
                    break
            if connected:
                break
            if (tcp_is_open("127.0.0.1", 8086) or tcp_is_open("127.0.0.1", 8087)) and not warned_editor_only:
                print("Detected LuckyEditor listener on 8086/8087; waiting for SDK gRPC endpoint...")
                warned_editor_only = True
            time.sleep(1.0)

        if not connected:
            if last_error:
                print(f"Last connection error: {last_error}")
            # Compatibility hint for the observed 2026.1 editor protocol mismatch.
            if tcp_is_open("127.0.0.1", 8086) or tcp_is_open("127.0.0.1", 8087):
                print("Detected LuckyEditor listener on 8086/8087, but no SDK-compatible gRPC endpoint.")
                print("This usually means gRPC server is not started yet, or an engine/SDK protocol mismatch.")
            print("Could not find an active LuckyEngine gRPC endpoint.")
            print("If LuckyEditor is open, start gRPC manually in the 'gRPC Server' panel, then rerun:")
            print("  make run-attach")
            sys.exit(1)

        print("Resetting scene...")
        reset_deadline = time.time() + max(10.0, args.reset_timeout)
        reconnect_attempted = False
        while True:
            try:
                session.reset()
                break
            except Exception as exc:
                msg = str(exc)
                not_ready = bool(
                    re.search(r"external agents not ready|scene still initializing|not ready", msg, re.IGNORECASE)
                )
                if not_ready and time.time() < reset_deadline:
                    print("Scene still initializing, retrying reset in 1s...")
                    time.sleep(1.0)
                    if not reconnect_attempted and time.time() + 30.0 > reset_deadline:
                        try:
                            print("Still waiting on external agents, reconnecting session once...")
                            session.close()
                            session = Session(host=host, port=port)
                            session.connect(timeout_s=max(2.0, min(args.connect_timeout, 15.0)), robot=args.robot)
                        except Exception:
                            pass
                        reconnect_attempted = True
                    continue
                raise

        config = session.get_robot_config(args.robot)
        action_dim = len(config["action_space"]["actuator_limits"])
        print(f"Connected. Action dimension: {action_dim}. Running control loop at {args.rate_hz} Hz.")

        step_idx = 0
        while True:
            session.step(np.zeros(action_dim))
            if step_idx % 20 == 0:
                print(f"Simulated step {step_idx}...")
            step_idx += 1
            time.sleep(period)
    except KeyboardInterrupt:
        print("\nShutdown requested by user.")
    except Exception as exc:
        print(f"\nSimulation process encountered an error: {exc}")
        sys.exit(1)
    finally:
        if session is not None:
            session.close()
        os.chdir(original_cwd)
        print("Application exit.")


if __name__ == "__main__":
    main()
