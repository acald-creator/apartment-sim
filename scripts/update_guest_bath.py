import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "guest_bath":
            room["coordinates"] = [39, 31]
            room["outline"] = [34.7, 22.5, 8.6, 17.0]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Reverted guest_bath back to [39, 31] in apartment.json")

if __name__ == "__main__":
    update()
