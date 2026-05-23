# Apartment Moving Simulator - 3D Bin Packing & Route Solver

A Python-based simulation utility that parses an apartment layout, schedules an optimal walkthrough route (solving the Traveling Salesman Problem), and packs inventory items into available shipping boxes using a 3D Bin Packing algorithm (First Fit Decreasing).

## Features

- **3D Bin Packing (First Fit Decreasing)**: Items are sorted by volume in descending order and placed into the first box where they geometrically fit (using up to 6 unique 3D rotations) and respect weight limits.
- **Guillotine Space Splitting**: Tracks empty cuboids inside boxes and splits remaining space cleanly without overlap.
- **Traveling Salesman Problem (TSP)**: Solves the exact shortest path between all rooms containing active items (starts and ends at the `entry` zone) to optimize the packing/cleaning order on moving day.
- **Unified Chronological Plan**: Generates a step-by-step room walkthrough detailing:
  - `[PACK]`: Items to be placed in specific boxes (with position/orientation info).
  - `[MOVE UNBOXED]`: Large furniture/appliances to wrap and carry directly.
  - `[DISCARD/REMOVE]`: Junk/unwanted items to carry to the dumpster.
  - `[LEAVE IN APARTMENT]`: Items that stay with the unit.

## Files

- `apartment.json`: JSON configuration of rooms, available box sizes, and the current inventory.
- `pack_items.py`: Evaluates and executes the 3D Bin Packing algorithm.
- `route_solver.py`: Solves the optimal room walkthrough using the exact TSP algorithm.
- `run_simulation.py`: The master runner script that runs both solvers and prints out the end-to-end moving plan.

## Requirements

- Python 3.x
- `Pillow` (Only needed if generating the coordinate map image; CLI simulation itself uses pure Python standard libraries).

## Usage

To run the complete chronological moving day simulation:

```bash
python3 run_simulation.py
```

To run only the 3D packing solver:

```bash
python3 pack_items.py
```

To run only the TSP routing solver:

```bash
python3 route_solver.py
```
