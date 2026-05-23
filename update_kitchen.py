import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "kitchen":
            room["coordinates"] = [67, 30]
            room["outline"] = [58.65, 22.45, 16.7, 15.1]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated kitchen in apartment.json to center [67, 30] and size [16.7, 15.1]")

if __name__ == "__main__":
    update()
