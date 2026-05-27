import os
import re

def list_imgui_windows():
    ini_path = "/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64/LuckyEditor/imgui.ini"
    if not os.path.exists(ini_path):
        print(f"Error: {ini_path} does not exist.")
        return

    print("Extracting ImGui window names from imgui.ini...")
    with open(ini_path, "r") as f:
        content = f.read()

    # Find [Window][...] patterns
    windows = re.findall(r'\[Window\]\[([^\]]+)\]', content)
    for w in sorted(list(set(windows))):
        print(f"  {w}")

if __name__ == "__main__":
    list_imgui_windows()
