import json
from pack_items import pack_items
from route_solver import solve_tsp, get_rooms_to_visit

def load_apartment(filename):
    with open(filename, "r") as f:
        return json.load(f)

def main():
    try:
        data = load_apartment("apartment.json")
    except FileNotFoundError:
        print("Error: apartment.json not found.")
        return

    # 1. Run Packing Simulation
    # Suppress internal prints of pack_items if any, but since it returns everything, we just unpack
    room_packages, used_boxes, unplaced_items = pack_items(data)

    # 2. Run Route Solver (TSP)
    rooms_coords = get_rooms_to_visit(data)
    path, total_dist = solve_tsp(rooms_coords, "entry")

    # 3. Compile inventories per room for all statuses (moved, stored, removed)
    inventory = data.get("inventory", [])
    
    # Track items by room and their placement status
    # We will map item_id to its packing info
    packed_info = {}
    for room, items in room_packages.items():
        for item in items:
            packed_info[item["item_id"]] = item

    print("=====================================================================")
    print("                HEADLESS MOVING SIMULATOR REPORT                     ")
    print("=====================================================================")
    print(f"Efficiency Route Distance: {total_dist:.2f} units")
    print(f"Total Boxes Used: {len(used_boxes)}")
    
    # Count box types
    box_counts = {}
    for box in used_boxes:
        box_counts[box["type"]] = box_counts.get(box["type"], 0) + 1
    for box_type, count in box_counts.items():
        print(f"  - {box_type.upper()}: {count} box(es)")
        
    print("=====================================================================")
    print("                      CHRONOLOGICAL MOVING PLAN                      ")
    print("=====================================================================")
    
    for step, room_id in enumerate(path, start=1):
        room_name = room_id.upper().replace('_', ' ')
        print(f"\nStep {step}: Go to {room_name}")
        
        # Get all items currently in this room
        room_items = [item for item in inventory if item["current_room"] == room_id]
        
        if not room_items and room_id != "entry":
            print("  - (No items to process in this room. Proceed to clean/inspect.)")
            continue
        elif room_id == "entry" and step == 1:
            print("  - [START] Prepare vehicle loading zone at Entryway.")
            # Show if there are any entry items
            if not room_items:
                continue
        elif room_id == "entry" and step == len(path):
            print("  - [FINISH] Final check complete. Load all remaining boxes onto truck.")
            continue
            
        # Group items by action
        for item in sorted(room_items, key=lambda x: x["id"]):
            item_id = item["id"]
            action = item.get("action", "move")
            fragile_tag = " [FRAGILE]" if item.get("fragile") else ""
            dims = item["dimensions_inches"]
            weight = item.get("weight_lbs", 5.0)
            
            if action == "move":
                if item_id in packed_info:
                    p = packed_info[item_id]
                    print(f"  [PACK] {item_id}{fragile_tag} ({dims[0]}x{dims[1]}x{dims[2]} in, {weight} lbs)")
                    print(f"         ──► Pack into {p['box_type'].upper()} Box #{p['box_index']}")
                    print(f"         ──► Orientation: {p['dimensions']} | Pos inside box: {p['position']}")
                else:
                    # Unboxed move item (furniture, large appliances)
                    print(f"  [MOVE UNBOXED] {item_id} ({dims[0]}x{dims[1]}x{dims[2]} in, {weight} lbs)")
                    print(f"                 ──► Wrap with moving blanket and load directly into truck")
            elif action == "remove":
                print(f"  [DISCARD/REMOVE] {item_id} ({dims[0]}x{dims[1]}x{dims[2]} in, {weight} lbs)")
                print(f"                   ──► Carry to dumpster or recycling bin")
            elif action == "store":
                print(f"  [LEAVE IN APARTMENT] {item_id} ({dims[0]}x{dims[1]}x{dims[2]} in, {weight} lbs)")
                print(f"                       ──► Leave in place (stays with the unit)")
                
    print("\n=====================================================================")
    print("                     END OF SIMULATION REPORT                        ")
    print("=====================================================================")

if __name__ == "__main__":
    main()
