import cv2
import os

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

# Create dataset directory if not exists
dataset_path = "datasets/face_samples"
os.makedirs(dataset_path, exist_ok=True)

# Start webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

face_id = input("Enter a Numeric User ID: ")
print("Capturing images... Look at the camera.")

count = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Save face images
        cv2.imwrite(f"{dataset_path}/face.{face_id}.{count}.jpg", gray[y:y+h, x:x+w])
        count += 1

    cv2.imshow("Face Capture", img)

    k = cv2.waitKey(100) & 0xFF
    if k == 27 or count >= 100:  # ESC to stop or 100 images captured
        break

print("Face data collection completed.")
cam.release()
cv2.destroyAllWindows()
