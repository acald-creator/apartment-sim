import json

def update():
    with open("apartment.json", "r") as f:
        data = json.load(f)

    for room in data["rooms"]:
        if room["id"] == "master_bath":
            room["coordinates"] = [67, 51]
            room["outline"] = [59.8, 44.8, 14.4, 12.4]
            break

    with open("apartment.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Updated master_bath in apartment.json to center [67, 51] and size [14.4, 12.4]")

if __name__ == "__main__":
    update()
