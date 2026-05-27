import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "bedroom_3_closet":
            room["coordinates"] = [32, 27]
            room["outline"] = [29.55, 20.5, 4.9, 13.0]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated bedroom_3_closet to [32, 27] in apartment.json")

if __name__ == "__main__":
    update()
