
import cv2

def count_faces(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,  # Try 1.05 or 1.03 for more accurate detection
    minNeighbors=5,    # Increase this value to reduce false positives
    minSize=(30, 30)   # Adjust based on the expected face size
)


    # Detect faces in the image
    # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Return the number of faces detected
    return len(faces)

if __name__ == "__main__":
    # Example usage
    # image_path = "/home/koddysmith/globalproject/RoomOccupancyMonitoringSystem/static/images/picture4.jpg"
    image_path = "/home/koddysmith/globalproject/RoomOccupancyMonitoringSystem/static/images/koddy.jpg"
    num_faces = count_faces(image_path)
    print(f"Number of faces detected: {num_faces}")
