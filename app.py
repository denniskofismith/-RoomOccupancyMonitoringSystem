from flask import Flask, render_template
import sqlite3
from facecount import count_faces
import os

app = Flask(__name__)

ROOM_CAPACITY = 100  # Define the total capacity of the room

def setup_database():

    db_path = 'motionlog.db'

    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS motionlog (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT,
                image_path TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print("Database and table created successfully")
    else:
        print("Database file already exists")



def get_latest_status():
    conn = sqlite3.connect('motionlog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM motionlog ORDER BY timestamp DESC LIMIT 1')
    row = cursor.fetchone()
    conn.close()
    return row


def determine_room_status(num_faces):

    occupancy_percentage = (num_faces / ROOM_CAPACITY) * 100
    if occupancy_percentage > 60:
        return 'Class Unavailable'
    else:
        return 'Class Available'




@app.route('/')
def index():
    data = get_latest_status()
    
    # Default status
    class_status = 'Class Available'
    timestamp = 'No data available'
    
    if data:
        timestamp, status, image_path = data[1], data[2], data[3]

        if status == 'Motion Detected' and image_path:

            num_faces = count_faces(image_path)
            # num_faces = 80
            
            
            class_status = determine_room_status(num_faces)
        
        # timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template('text.html', class_status=class_status, timestamp=timestamp,num_faces=num_faces)

 

if __name__ == "__main__":
    setup_database()

    app.run(debug=True)
