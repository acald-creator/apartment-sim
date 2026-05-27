#!/usr/bin/env python3
"""Continuously probe likely LuckyEngine gRPC endpoints."""

import argparse
import socket
import time


def parse_port_spec(spec: str) -> list[int]:
    if "-" in spec:
        a, b = spec.split("-", 1)
        start = int(a)
        end = int(b)
        if end < start:
            start, end = end, start
        return list(range(start, end + 1))
    return [int(spec)]


def can_connect(host: str, port: int, timeout_s: float = 0.25) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout_s):
            return True
    except OSError:
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hosts", type=str, default="127.0.0.1,localhost,172.24.160.1")
    parser.add_argument("--ports", type=str, default="50051-50060")
    parser.add_argument("--interval", type=float, default=1.0)
    args = parser.parse_args()

    hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    ports = parse_port_spec(args.ports)

    print(f"Probing hosts={hosts} ports={ports[0]}..{ports[-1]} every {args.interval:.1f}s", flush=True)
    print("Press Ctrl+C to stop.", flush=True)

    try:
        while True:
            found = []
            for host in hosts:
                for port in ports:
                    if can_connect(host, port):
                        found.append((host, port))
            if found:
                items = ", ".join([f"{h}:{p}" for h, p in found])
                print(f"[OPEN] {items}", flush=True)
            else:
                print("[OPEN] none", flush=True)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nStopped.", flush=True)


if __name__ == "__main__":
    main()
