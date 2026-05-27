import json

def update():
    updated_rooms = {
        "bedroom_1_master": {
            "coordinates": [70, 68],
            "outline": [58.45, 57.45, 23.1, 21.1]
        },
        "bedroom_3_closet": {
            "coordinates": [31, 27],
            "outline": [27.36, 22.25, 7.29, 9.5]
        },
        "linen_closet": {
            "coordinates": [33, 56],
            "outline": [30.9, 52.45, 4.2, 7.1]
        },
        "utility_room": {
            "coordinates": [80, 30],
            "outline": [76.05, 22.8, 7.9, 14.4]
        },
        "entry_closet": {
            "coordinates": [74, 36],
            "outline": [71.9, 34.2, 4.2, 3.6]
        }
    }

    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        rid = room["id"]
        if rid in updated_rooms:
            room["coordinates"] = updated_rooms[rid]["coordinates"]
            room["outline"] = updated_rooms[rid]["outline"]

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated coordinates/outlines for multiple rooms in apartment.json")

if __name__ == "__main__":
    update()
