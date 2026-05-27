SHELL := /usr/bin/env bash

.PHONY: setup run run-attach run-launch run-smoke editor probe-grpc scene-from-image

setup:
	./setup.sh

run:
	source .venv/bin/activate && python run_lucky_robots.py --skip-launch

run-launch:
	source .venv/bin/activate && python run_lucky_robots.py

run-smoke:
	source .venv/bin/activate && python run_lucky_robots.py --robot unitreego2 --scene velocity --task locomotion --connect-timeout 30 --reset-timeout 180

editor:
	cd /home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64/LuckyEditor && \
	export DOTNET_ROOT=/usr/lib/dotnet && \
	export PATH=/usr/bin:$$PATH && \
	export LD_LIBRARY_PATH=/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64/lib:$$LD_LIBRARY_PATH && \
	/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64/bin/LuckyEditor RobotSandbox/RobotSandbox.hproj

run-attach:
	source .venv/bin/activate && python run_lucky_robots.py --skip-launch

probe-grpc:
	source .venv/bin/activate && python scripts/grpc_probe.py

scene-from-image:
	source .venv/bin/activate && python scripts/generate_scene_from_floorplan.py
