import time
from gpiozero import MotionSensor
import sqlite3
import subprocess
from datetime import datetime

# Configure your PIR sensor
PIR_PIN = 17  # Change this to the GPIO pin you're using
pir = MotionSensor(PIR_PIN)

def setup_database():
    conn = sqlite3.connect('motionlog.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS motionlog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            status TEXT,
            image_path TEXT  -- Column to store the path of the captured image
        )
    ''')
    conn.commit()
    conn.close()
    print("Table created successfully")

def log_motion_status(status, image_path=None):
    conn = sqlite3.connect('motionlog.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO motionlog (timestamp, status, image_path)
        VALUES (?, ?, ?)
    ''', (datetime.now(), status, image_path))
    conn.commit()
    conn.close()

def capture_image():
    # Generate a filename with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"/home/koddysmith/globalproject/RoomOccupancyMonitoringSystem/static/images/{timestamp}.jpg"

    # Command to execute
    command = ["libcamera-still", "-o", output_file]
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Image captured and saved as {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to capture image: {e}")
        return None

    return output_file

def monitor_motion():
    while True:
        # Wait for motion
        pir.wait_for_active()
        print("Motion detected")
        image_path = capture_image()
        log_motion_status("Motion Detected", image_path)
        
        time.sleep(5)

        # Wait until there's no motion
        pir.wait_for_inactive()
        print('No Motion Detected')
        # log_motion_status("No Motion Detected")

        # Sleep to prevent multiple triggers within a short time
        time.sleep(0.5)

if __name__ == "__main__":
    setup_database()  # Ensure the database table is set up
    monitor_motion()  # Start monitoring for motion
