import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "master_closet":
            room["coordinates"] = [78, 51]
            room["outline"] = [74.0, 44.85, 8.0, 12.3]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated master_closet in apartment.json to center [78, 51] and size [8.0, 12.3]")

if __name__ == "__main__":
    update()
