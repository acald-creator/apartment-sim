import json
from itertools import permutations

def load_apartment(filename):
    """Loads apartment data from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)

def volume(dimensions):
    """Calculates the volume of a 3D cuboid."""
    return dimensions[0] * dimensions[1] * dimensions[2]

def get_rotations(dimensions):
    """Returns all unique 3D rotations (permutations) of the given dimensions."""
    return list(set(permutations(dimensions)))

def split_free_space(free_space, item_dims):
    """
    Splits a free cuboid after placing an item at the origin (x, y, z) of the free space.
    Uses the Guillotine split method to produce 3 non-overlapping smaller cuboids.
    """
    x, y, z = free_space["x"], free_space["y"], free_space["z"]
    dx, dy, dz = free_space["dx"], free_space["dy"], free_space["dz"]
    w, d, h = item_dims

    new_spaces = []
    
    # 1. Right space (along x-axis)
    if dx > w:
        new_spaces.append({
            "x": x + w,
            "y": y,
            "z": z,
            "dx": dx - w,
            "dy": dy,
            "dz": dz
        })
    
    # 2. Front space (along y-axis)
    # Occupies the width of the placed item, but covers the remaining depth
    if dy > d:
        new_spaces.append({
            "x": x,
            "y": y + d,
            "z": z,
            "dx": w,
            "dy": dy - d,
            "dz": dz
        })
        
    # 3. Above space (along z-axis)
    # Occupies only the width and depth of the placed item, but covers the remaining height
    if dz > h:
        new_spaces.append({
            "x": x,
            "y": y,
            "z": z + h,
            "dx": w,
            "dy": d,
            "dz": dz - h
        })
        
    return new_spaces

def pack_items(data):
    rooms = data.get("rooms", [])
    boxes = data.get("boxes", [])
    inventory = data.get("inventory", [])

    # Map item ID to its details (like room) for final grouping
    item_to_room = {item["id"]: item["current_room"] for item in inventory}

    # Sort items by volume in decreasing order (First Fit Decreasing)
    sorted_inventory = sorted(
        inventory, key=lambda x: volume(x["dimensions_inches"]), reverse=True
    )

    used_boxes = []
    unplaced_items = []

    for item in sorted_inventory:
        item_id = item["id"]
        item_dims = item["dimensions_inches"]
        # Default to 5.0 lbs if weight_lbs is not specified in the input JSON
        item_weight = item.get("weight_lbs", 5.0)
        fragile = item.get("fragile", False)
        placed = False

        # Try to fit the item in existing boxes
        for box in used_boxes:
            # Check weight limit first
            current_weight = sum(it["weight"] for it in box["items"])
            if current_weight + item_weight > box["max_weight"]:
                continue

            # Try to place the item in one of the free spaces of this box
            for i, free_space in enumerate(box["free_spaces"]):
                # Try all unique orientations/rotations of the item
                for rotation in get_rotations(item_dims):
                    w, d, h = rotation
                    if w <= free_space["dx"] and d <= free_space["dy"] and h <= free_space["dz"]:
                        # Item fits in this orientation! Place it here
                        box["items"].append({
                            "id": item_id,
                            "position": (free_space["x"], free_space["y"], free_space["z"]),
                            "dimensions": rotation,
                            "weight": item_weight,
                            "fragile": fragile
                        })
                        
                        # Split the remaining space
                        new_spaces = split_free_space(free_space, rotation)
                        
                        # Remove the old free space and append the new split spaces
                        box["free_spaces"].pop(i)
                        box["free_spaces"].extend(new_spaces)
                        
                        placed = True
                        break # Break out of rotation check
                if placed:
                    break # Break out of free space check
            if placed:
                break # Break out of box check

        # If it didn't fit in any existing box, open a new box of the smallest possible type
        if not placed:
            # Sort available box types by volume ascending
            sorted_box_types = sorted(boxes, key=lambda b: volume(b["dimensions_inches"]))
            for box_type in sorted_box_types:
                # Check if the box can support the item's weight
                if box_type["max_weight_lbs"] < item_weight:
                    continue
                
                # Check if the item can fit in the box's outer dimensions (under any rotation)
                box_dims = box_type["dimensions_inches"]
                for rotation in get_rotations(item_dims):
                    w, d, h = rotation
                    if w <= box_dims[0] and d <= box_dims[1] and h <= box_dims[2]:
                        # Create the new box
                        new_box = {
                            "type": box_type["type"],
                            "dimensions": box_dims,
                            "max_weight": box_type["max_weight_lbs"],
                            "free_spaces": [
                                {
                                    "x": 0,
                                    "y": 0,
                                    "z": 0,
                                    "dx": box_dims[0],
                                    "dy": box_dims[1],
                                    "dz": box_dims[2]
                                }
                            ],
                            "items": []
                        }
                        
                        # Place the item in the new box at (0, 0, 0)
                        new_box["items"].append({
                            "id": item_id,
                            "position": (0, 0, 0),
                            "dimensions": rotation,
                            "weight": item_weight,
                            "fragile": fragile
                        })
                        
                        # Split the initial free space
                        initial_space = new_box["free_spaces"].pop(0)
                        new_spaces = split_free_space(initial_space, rotation)
                        new_box["free_spaces"].extend(new_spaces)
                        
                        used_boxes.append(new_box)
                        placed = True
                        break
                if placed:
                    break

        if not placed:
            unplaced_items.append(item)

    # Group packed items by room they started in
    room_packages = {room["id"]: [] for room in rooms}
    # Add a fallback key in case rooms in JSON don't list a room, though they should
    for box_idx, box in enumerate(used_boxes, start=1):
        for item in box["items"]:
            room = item_to_room.get(item["id"], "unknown")
            if room not in room_packages:
                room_packages[room] = []
            room_packages[room].append({
                "item_id": item["id"],
                "box_type": box["type"],
                "box_index": box_idx,
                "position": item["position"],
                "dimensions": item["dimensions"],
                "fragile": item["fragile"]
            })

    return room_packages, used_boxes, unplaced_items

def main():
    # Load apartment details
    try:
        data = load_apartment("apartment.json")
    except FileNotFoundError:
        print("Error: apartment.json not found in current directory.")
        return

    # Run packing algorithm
    room_packages, used_boxes, unplaced_items = pack_items(data)

    # Print warnings for unpacked items
    for item in unplaced_items:
        print(f"Warning: Could not place item '{item['id']}' (dimensions: {item['dimensions_inches']}, weight: {item.get('weight_lbs', 5.0)} lbs) in any available box type.")

    # Print out a final packaging list grouped by starting room
    print("=========================================")
    print("      MOVING SIMULATOR PACKING LIST      ")
    print("=========================================")
    
    for room, packed_items in sorted(room_packages.items()):
        print(f"\nRoom: {room.upper().replace('_', ' ')}")
        if not packed_items:
            print("  (No items packed)")
            continue
            
        for item in packed_items:
            fragile_tag = " [FRAGILE]" if item["fragile"] else ""
            print(f"  - {item['item_id']}{fragile_tag}")
            print(f"    Packed in: {item['box_type'].upper()} box #{item['box_index']}")
            print(f"    Placement position: {item['position']} | Packed dimensions: {item['dimensions']}")

if __name__ == "__main__":
    main()
