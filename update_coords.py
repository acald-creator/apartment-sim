import json

def update():
    updated_coords = {
        "bedroom_3_closet": [17, 27],
        "guest_bath": [32, 28],
        "linen_closet": [32, 36],
        "bedroom_2_closet": [18, 51],
        "living_room": [50, 56],
        "master_bath": [66, 51],
        "master_closet": [78, 51],
        "bedroom_1_master": [71, 69],
        "entry_closet": [74, 36],
        "utility_room": [80, 30],
        "kitchen": [67, 30]
    }

    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        rid = room["id"]
        if rid in updated_coords:
            new_cx, new_cy = updated_coords[rid]
            room["coordinates"] = [new_cx, new_cy]
            
            w = room["outline"][2]
            h = room["outline"][3]
            
            if rid == "bedroom_3_closet":
                w = 8.0
                h = 13.0
            elif rid == "bedroom_2_closet":
                w = 11.5
                h = 11.0
            elif rid == "master_closet":
                w = 4.2
                h = 10.0
                
            new_ox = round(new_cx - w/2, 2)
            new_oy = round(new_cy - h/2, 2)
            room["outline"] = [new_ox, new_oy, w, h]

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Successfully updated apartment.json rooms")

if __name__ == "__main__":
    update()
