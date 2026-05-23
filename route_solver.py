import json
import math
from itertools import permutations

def load_apartment(filename):
    with open(filename, "r") as f:
        return json.load(f)

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def solve_tsp(rooms_dict, start_room_id="entry"):
    """
    Finds the exact optimal TSP tour starting and ending at start_room_id.
    Returns the ordered list of room IDs and the total distance.
    """
    room_ids = list(rooms_dict.keys())
    if start_room_id not in room_ids:
        raise ValueError(f"Start room '{start_room_id}' not found in rooms.")
        
    other_rooms = [r for r in room_ids if r != start_room_id]
    
    if not other_rooms:
        return [start_room_id], 0.0
        
    best_distance = float("inf")
    best_path = None
    
    start_coords = rooms_dict[start_room_id]
    
    # Brute-force search over all permutations of other rooms
    for perm in permutations(other_rooms):
        current_distance = 0.0
        prev_coords = start_coords
        
        # Distance from start to first room, and then through all rooms
        for room_id in perm:
            curr_coords = rooms_dict[room_id]
            current_distance += calculate_distance(prev_coords, curr_coords)
            prev_coords = curr_coords
            
        # Distance back to start room
        current_distance += calculate_distance(prev_coords, start_coords)
        
        if current_distance < best_distance:
            best_distance = current_distance
            best_path = (start_room_id,) + perm + (start_room_id,)
            
    return list(best_path), best_distance

def get_rooms_to_visit(data):
    """
    Identifies which rooms contain items that need to be moved or removed.
    Always includes the entry room.
    """
    rooms = data.get("rooms", [])
    inventory = data.get("inventory", [])
    
    # Find rooms with items to pack (action: move) or clear (action: remove)
    active_rooms = set()
    for item in inventory:
        if item.get("action") in ["move", "remove"]:
            active_rooms.add(item["current_room"])
            
    # Always include entry as the starting loading zone
    active_rooms.add("entry")
    
    # Map room ID to coordinates
    rooms_coords = {r["id"]: r["coordinates"] for r in rooms if r["id"] in active_rooms}
    return rooms_coords

def main():
    try:
        data = load_apartment("apartment.json")
    except FileNotFoundError:
        print("Error: apartment.json not found.")
        return
        
    rooms_coords = get_rooms_to_visit(data)
    
    print("=========================================")
    # Print coordinates of rooms being visited
    print("Rooms to visit for moving/cleaning:")
    for room, coords in sorted(rooms_coords.items()):
        print(f"  - {room.upper().replace('_', ' ')}: {coords}")
        
    path, total_dist = solve_tsp(rooms_coords, "entry")
    
    print("\n=========================================")
    print("      OPTIMAL MOVING ROUTE (TSP SOLVER)   ")
    print("=========================================")
    print(f"Total Optimal Route Distance: {total_dist:.2f} units")
    print("\nVisit Order:")
    for i, room in enumerate(path, start=1):
        arrow = " ──►" if i < len(path) else ""
        print(f"  {i}. {room.upper().replace('_', ' ')}{arrow}")

if __name__ == "__main__":
    main()
