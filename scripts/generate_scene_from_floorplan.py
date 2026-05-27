#!/usr/bin/env python3
"""Generate a native LuckyEngine mesh scene from a floorplan image.

This script detects major horizontal/vertical wall lines from a 2D floorplan
image and emits a mesh-based `.hscene` with simple 3D wall blocks.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re

import cv2
import numpy as np


DEFAULT_ENGINE_ROOT = Path(
    "/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64"
)
DEFAULT_IMAGE = Path(
    "/home/acald-creator/go/src/github.com/acald-creator/apartment-moving-simulator/3x2_islandpark_14c1 2d- resied (square).webp"
)
DEFAULT_SCENE_NAME = "ApartmentFromImage.hscene"
CUBE_ASSET_ID = 636035523334520015


def detect_axis_aligned_lines(
    image_path: Path,
    threshold: int = 130,
    min_len_px: int = 40,
    merge_gap_px: int = 6,
) -> list[tuple[str, float, float, float]]:
    """Return axis-aligned wall segments as (axis, x_or_y, start, end)."""
    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise RuntimeError(f"Could not read image: {image_path}")

    # Invert threshold so dark walls become white foreground.
    _, bw = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
    bw = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))

    lines = cv2.HoughLinesP(
        bw,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=min_len_px,
        maxLineGap=10,
    )
    if lines is None:
        return []

    # Normalize as horizontal/vertical only.
    horiz: list[tuple[float, float, float]] = []  # y, x1, x2
    vert: list[tuple[float, float, float]] = []  # x, y1, y2
    for line in lines[:, 0, :]:
        x1, y1, x2, y2 = map(float, line.tolist())
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        if dx < 1 and dy < 1:
            continue
        if dx >= 3 * max(dy, 1):
            y = (y1 + y2) / 2.0
            horiz.append((y, min(x1, x2), max(x1, x2)))
        elif dy >= 3 * max(dx, 1):
            x = (x1 + x2) / 2.0
            vert.append((x, min(y1, y2), max(y1, y2)))

    def merge_parallel(
        entries: list[tuple[float, float, float]]
    ) -> list[tuple[float, float, float]]:
        if not entries:
            return []
        # group by axis coordinate proximity
        entries.sort(key=lambda t: (t[0], t[1], t[2]))
        groups: list[list[tuple[float, float, float]]] = []
        for e in entries:
            if not groups or abs(e[0] - groups[-1][0][0]) > merge_gap_px:
                groups.append([e])
            else:
                groups[-1].append(e)

        merged: list[tuple[float, float, float]] = []
        for g in groups:
            axis = float(np.mean([x[0] for x in g]))
            segs = sorted([(x[1], x[2]) for x in g], key=lambda p: p[0])
            cur_s, cur_e = segs[0]
            for s, e in segs[1:]:
                if s <= cur_e + merge_gap_px:
                    cur_e = max(cur_e, e)
                else:
                    merged.append((axis, cur_s, cur_e))
                    cur_s, cur_e = s, e
            merged.append((axis, cur_s, cur_e))
        return merged

    horiz_m = merge_parallel(horiz)
    vert_m = merge_parallel(vert)

    # Keep meaningful segments only.
    out: list[tuple[str, float, float, float]] = []
    for y, x1, x2 in horiz_m:
        if x2 - x1 >= min_len_px:
            out.append(("h", y, x1, x2))
    for x, y1, y2 in vert_m:
        if y2 - y1 >= min_len_px:
            out.append(("v", x, y1, y2))
    return out


def write_hscene(
    scene_path: Path,
    segments: list[tuple[str, float, float, float]],
    image_w: int,
    image_h: int,
    meters_per_pixel: float = 0.03,
) -> None:
    cx = image_w / 2.0
    cy = image_h / 2.0

    def map_xy(px: float, py: float) -> tuple[float, float]:
        # Image -> world: x right, y up
        wx = (px - cx) * meters_per_pixel
        wy = (cy - py) * meters_per_pixel
        return wx, wy

    lines: list[str] = []
    lines.append("Scene: LuckyRobots")
    lines.append("SceneSettings:")
    lines.append("  SceneTimeMode: 1")
    lines.append("  FreeStepEnabled: false")
    lines.append("  TimeRunners:")
    lines.append("    - ID: 0")
    lines.append("      Name: Robot")
    lines.append("      Frequency: 50")
    lines.append("      Locked: false")
    lines.append("  OnUpdateSettings:")
    lines.append("    Enabled: true")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 0")
    lines.append("    Phase: 1")
    lines.append("  OnPhysicsUpdateSettings:")
    lines.append("    Enabled: true")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 0")
    lines.append("    Phase: 2")
    lines.append("  OnLateUpdateSettings:")
    lines.append("    Enabled: true")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 0")
    lines.append("    Phase: 3")
    lines.append("  UpdateAnimationSettings:")
    lines.append("    Enabled: true")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 100")
    lines.append("    Phase: 3")
    lines.append("  Box2DSettings:")
    lines.append("    Enabled: false")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 0")
    lines.append("    Phase: 2")
    lines.append("  JoltSettings:")
    lines.append("    Enabled: true")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 0")
    lines.append("    Phase: 2")
    lines.append("  MujocoSettings:")
    lines.append("    Enabled: false")
    lines.append("    RunnerID: 0")
    lines.append("    RunnerName: Robot")
    lines.append("    Frequency: 50")
    lines.append("    Priority: 0")
    lines.append("    Phase: 2")
    lines.append("    CollisionCheckingEnabled: false")
    lines.append("PrefabManager: []")
    lines.append("Entities:")

    eid = 9903000000000000000

    def add_entity(tag: str, px: float, py: float, pz: float, sx: float, sy: float, sz: float) -> None:
        nonlocal eid
        lines.append(f"  - Entity: {eid}")
        lines.append("    Domain: Client")
        lines.append("    TagComponent:")
        lines.append(f"      Tag: {tag}")
        lines.append("    Parent: 0")
        lines.append("    Children:")
        lines.append("      []")
        lines.append("    TransformComponent:")
        lines.append(f"      Position: [{px:.6f}, {py:.6f}, {pz:.6f}]")
        lines.append("      Rotation: [0, 0, 0]")
        lines.append(f"      Scale: [{sx:.6f}, {sy:.6f}, {sz:.6f}]")
        lines.append("    StaticMeshComponent:")
        lines.append(f"      AssetID: {CUBE_ASSET_ID}")
        lines.append("      MaterialTable:")
        lines.append("        0: 0")
        lines.append("      Visible: true")
        eid += 1

    # Camera
    lines.extend(
        [
            f"  - Entity: {eid}",
            "    Domain: Client",
            "    TagComponent:",
            "      Tag: Main Camera",
            "    Parent: 0",
            "    Children:",
            "      []",
            "    TransformComponent:",
            "      Position: [0.0, 8.0, -16.0]",
            "      Rotation: [2.75, 0, 3.14159226]",
            "      Scale: [1, 1, 1]",
            "    CameraComponent:",
            "      Camera:",
            "        ProjectionType: 0",
            "        PerspectiveFOV: 60",
            "        PerspectiveNear: 0.1",
            "        PerspectiveFar: 4000",
            "        OrthographicSize: 10",
            "        OrthographicNear: -1",
            "        OrthographicFar: 1",
            "      Primary: true",
        ]
    )
    eid += 1

    # Light
    lines.extend(
        [
            f"  - Entity: {eid}",
            "    Domain: Client",
            "    TagComponent:",
            "      Tag: Directional Light",
            "    Parent: 0",
            "    Children:",
            "      []",
            "    TransformComponent:",
            "      Position: [0, 0, 0]",
            "      Rotation: [1.2, 0.4, -1.2]",
            "      Scale: [1, 1, 1]",
            "    DirectionalLightComponent:",
            "      Intensity: 2.0",
            "      Radiance: [1, 1, 1]",
            "      CastShadows: true",
            "      SoftShadows: true",
            "      LightSize: 0.5",
            "      ShadowAmount: 1",
        ]
    )
    eid += 1

    # Ground slab
    wx = image_w * meters_per_pixel
    wy = image_h * meters_per_pixel
    add_entity("Ground", 0.0, 0.0, -0.10, wx, wy, 0.20)

    wall_thickness = 0.24
    wall_height = 2.8

    for idx, (axis, fixed, start, end) in enumerate(segments):
        if axis == "h":
            x1, y = map_xy(start, fixed)
            x2, _ = map_xy(end, fixed)
            cx_w = (x1 + x2) / 2.0
            length = abs(x2 - x1)
            add_entity(f"WallH_{idx}", cx_w, y, wall_height / 2.0, length, wall_thickness, wall_height)
        else:
            x, y1 = map_xy(fixed, start)
            _, y2 = map_xy(fixed, end)
            cy_w = (y1 + y2) / 2.0
            length = abs(y2 - y1)
            add_entity(f"WallV_{idx}", x, cy_w, wall_height / 2.0, wall_thickness, length, wall_height)

    scene_path.write_text("\n".join(lines) + "\n")


def set_start_scene(project_file: Path, scene_name: str) -> None:
    txt = project_file.read_text()
    txt = re.sub(
        r"^\s*StartScene:.*$",
        f"  StartScene: Scenes/{scene_name}",
        txt,
        flags=re.MULTILINE,
    )
    project_file.write_text(txt)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", type=Path, default=DEFAULT_IMAGE)
    parser.add_argument("--engine-root", type=Path, default=DEFAULT_ENGINE_ROOT)
    parser.add_argument("--scene-name", type=str, default=DEFAULT_SCENE_NAME)
    parser.add_argument("--meters-per-pixel", type=float, default=0.03)
    args = parser.parse_args()

    image = cv2.imread(str(args.image), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise SystemExit(f"Could not read image: {args.image}")
    h, w = image.shape

    segments = detect_axis_aligned_lines(args.image)
    if not segments:
        raise SystemExit("No wall segments detected from image.")

    scene_path = (
        args.engine_root
        / "LuckyEditor"
        / "RobotSandbox"
        / "Assets"
        / "Scenes"
        / args.scene_name
    )
    project_path = args.engine_root / "LuckyEditor" / "RobotSandbox" / "RobotSandbox.hproj"

    write_hscene(scene_path, segments, w, h, meters_per_pixel=args.meters_per_pixel)
    set_start_scene(project_path, args.scene_name)

    print(f"Wrote scene: {scene_path}")
    print(f"Detected wall segments: {len(segments)}")
    print(f"Updated StartScene to: Scenes/{args.scene_name}")


if __name__ == "__main__":
    main()
