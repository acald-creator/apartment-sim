import json
import re

def sync():
    with open("apartment.json", "r") as f:
        data = json.load(f)
        
    rooms = data["rooms"]
    
    # Format each room nicely on a single line
    rooms_str_list = []
    for r in rooms:
        # e.g. {"id": "utility_room", "coordinates": [80, 30], "outline": [77.5, 22.5, 5.0, 15.0]}
        coord_str = f"[{r['coordinates'][0]}, {r['coordinates'][1]}]"
        outline_str = f"[{r['outline'][0]}, {r['outline'][1]}, {r['outline'][2]}, {r['outline'][3]}]"
        room_line = f'{{"id": "{r["id"]}", "coordinates": {coord_str}, "outline": {outline_str}}}'
        rooms_str_list.append(room_line)
        
    rooms_js = "[\n                " + ",\n                ".join(rooms_str_list) + "\n            ]"
    
    with open("index.html", "r") as f:
        html = f.read()
        
    # We want to replace the rooms field in DEFAULT_CONFIG
    # Matches "rooms": [ ... ] inside DEFAULT_CONFIG
    pattern = r'("rooms"\s*:\s*\[.*?\]\s*,?\s*)\n\s*"boxes"'
    
    # Let's perform regex replacement
    replacement = f'"rooms": {rooms_js},\n            "boxes"'
    html_new = re.sub(pattern, replacement, html, flags=re.DOTALL)
    
    with open("index.html", "w") as f:
        f.write(html_new)
        
    print("Successfully synchronized index.html DEFAULT_CONFIG.rooms")

if __name__ == "__main__":
    sync()
