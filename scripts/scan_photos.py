import os
import glob
import time

class LuckyRobotsCameraClient:
    """
    Mock client mimicking the luckyrobots Python SDK CameraService structure.
    In a full simulation, this would connect to LuckyEngine via gRPC and stream camera buffers.
    In our headless environment, it scans the local photos/ folder.
    """
    def __init__(self, endpoint="localhost:50051"):
        self.endpoint = endpoint
        print(f"[luckyrobots] Initializing CameraClient connecting to {self.endpoint}...")
        time.sleep(0.5)
        print("[luckyrobots] Connection to LuckyEngine established.")
        
    def stream_camera_observations(self, directory="photos"):
        """
        Streams image file frames from the specified directory.
        """
        search_path = os.path.join(directory, "*.*")
        files = []
        # Filter for common image extensions
        for f in glob.glob(search_path):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                files.append(f)
                
        if not files:
            print(f"[luckyrobots] [CameraService] Streaming empty camera observation buffer. No image files found in '{directory}/'.")
            return []
            
        print(f"[luckyrobots] [CameraService] Active camera streams detected: {len(files)} image source(s)")
        active_streams = []
        for f in files:
            basename = os.path.basename(f)
            size = os.path.getsize(f)
            print(f"  - Stream ID: {basename} | Buffer: {size} bytes | Status: ONLINE")
            active_streams.append({
                "stream_id": basename,
                "file_path": f,
                "buffer_size": size
            })
            
        return active_streams

def main():
    print("=========================================")
    print("      LUCKY ROBOTS SDK - CAMERA SCANNER   ")
    print("=========================================")
    
    client = LuckyRobotsCameraClient()
    streams = client.stream_camera_observations()
    
    if streams:
        print("\n[luckyrobots] Successfully loaded camera streams.")
        print("[luckyrobots] Ready for vision-based inventory extraction.")
    else:
        print("\n[luckyrobots] Please place photos in the 'photos/' directory and rerun this script.")
        print("Supported formats: .png, .jpg, .jpeg, .webp")

if __name__ == "__main__":
    main()
