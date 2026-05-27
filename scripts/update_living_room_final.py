import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "living_room":
            room["coordinates"] = [50, 55]
            room["outline"] = [41.25, 43.85, 17.5, 22.3]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated living_room in apartment.json to center [50, 55] and size [17.5, 22.3]")

if __name__ == "__main__":
    update()
