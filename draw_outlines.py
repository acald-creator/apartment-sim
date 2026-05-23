import json
from PIL import Image, ImageDraw, ImageFont

def draw_outlines():
    # Load image
    img_path = "3x2_islandpark_14c1 2d- resied (square).webp"
    try:
        img = Image.open(img_path).convert("RGBA")
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # Load JSON
    try:
        with open("apartment.json", "r") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading json: {e}")
        return

    draw = ImageDraw.Draw(img)
    w, h = img.size

    for room in data.get("rooms", []):
        outline = room.get("outline")
        if outline:
            # Scale percent coordinates to pixels
            x1 = (outline[0] / 100.0) * w
            y1 = (outline[1] / 100.0) * h
            x2 = ((outline[0] + outline[2]) / 100.0) * w
            y2 = ((outline[1] + outline[3]) / 100.0) * h

            # Draw rectangle
            draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
            
            # Draw label
            draw.text((x1 + 4, y1 + 4), room["id"], fill="blue")

    img.save("floorplan_with_outlines.png")
    print("Saved floorplan_with_outlines.png")

if __name__ == "__main__":
    draw_outlines()
