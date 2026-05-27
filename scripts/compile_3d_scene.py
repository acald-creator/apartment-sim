import os
import shutil

DEFAULT_ENGINE_ROOT = "/home/acald-creator/go/src/github.com/acald-creator/LuckyEngine-2026.1-Linux-x64"


def resolve_engine_root():
    return os.environ.get("LUCKYENGINE_PATH") or os.environ.get("LUCKYENGINE_HOME") or DEFAULT_ENGINE_ROOT


def copy_scene_xml():
    engine_path = resolve_engine_root()
    src_xml = "apartment_3d.xml"
    dest_dir = os.path.join(engine_path, "LuckyEditor", "RobotSandbox", "Assets")
    dest_xml = os.path.join(dest_dir, "apartment_3d.xml")

    if not os.path.exists(src_xml):
        print(f"Error: Source scene {src_xml} does not exist.")
        return False

    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory {dest_dir} does not exist. Check LUCKYENGINE_PATH.")
        return False

    try:
        shutil.copy2(src_xml, dest_xml)
        print(f"Successfully copied {src_xml} -> {dest_xml}")
        print("Scene key for runner launch is: apartment_3d")
        return True
    except Exception as e:
        print(f"Error copying {src_xml} to {dest_xml}: {e}")
        return False

def dump_latest_logs():
    engine_path = resolve_engine_root()
    config_log_path = "lucky_engine_config.log"
    
    hazel_log_p = os.path.join(engine_path, "LuckyEditor", "logs", "HAZEL.log")
    app_log_p = os.path.join(engine_path, "LuckyEditor", "logs", "APP.log")
    
    with open(config_log_path, "w") as log_f:
        if os.path.exists(hazel_log_p):
            log_f.write(f"=== HAZEL.log ({hazel_log_p}) ===\n")
            with open(hazel_log_p, "r", encoding="utf-8", errors="ignore") as hz_f:
                lines = hz_f.readlines()
                log_f.write("".join(lines[-500:]))
            log_f.write("\n\n")
        else:
            log_f.write(f"=== HAZEL.log NOT FOUND at {hazel_log_p} ===\n\n")

        if os.path.exists(app_log_p):
            log_f.write(f"=== APP.log ({app_log_p}) ===\n")
            with open(app_log_p, "r", encoding="utf-8", errors="ignore") as app_f:
                lines = app_f.readlines()
                log_f.write("".join(lines[-500:]))
            log_f.write("\n\n")
        else:
            log_f.write(f"=== APP.log NOT FOUND at {app_log_p} ===\n\n")

    print(f"Latest logs dumped to {config_log_path}")

if __name__ == "__main__":
    copy_scene_xml()
    dump_latest_logs()
