
import time
from gpiozero import MotionSensor
import sqlite3

# Configure your PIR sensor
PIR_PIN = 17  # Change this to the GPIO pin you're using
pir = MotionSensor(PIR_PIN)

def log_motion_status(status):
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO motion_log (status)
        VALUES (?)
    ''', (status,))
    conn.commit()
    conn.close()

def monitor_motion():


    while True:

        status = [] 
        # Wait for 5 minutes
        time.sleep(0.5)
        
        pir.wait_for_active()
        print("Motion detected")
        status.append("Motion Detected")
        log_motion_status(status[-1])
        print(status)

        time.sleep(10)
        
        pir.wait_for_inactive()
        print('No Motion Detected')
        status.append("No Motion Detected")
        log_motion_status(status[-1])
        print(status)



if __name__ == "__main__":
    monitor_motion()
