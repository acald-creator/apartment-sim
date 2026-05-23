import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "living_room":
            room["coordinates"] = [50, 53]
            room["outline"] = [40.5, 39.5, 18.75, 27.0]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated living_room in apartment.json")

if __name__ == "__main__":
    update()
