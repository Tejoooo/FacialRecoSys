import cv2
import numpy as np
from PIL import Image
import os

dataset_path = "datasets/face_samples"
trainer_path = "models/trainer.yml"

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")

def get_images_and_labels():
    image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path)]
    faces, ids = [], []

    for image_path in image_paths:
        gray_img = Image.open(image_path).convert("L")
        img_arr = np.array(gray_img, "uint8")

        user_id = int(os.path.split(image_path)[-1].split(".")[1])
        detected_faces = face_cascade.detectMultiScale(img_arr)

        for (x, y, w, h) in detected_faces:
            faces.append(img_arr[y:y+h, x:x+w])
            ids.append(user_id)

    return faces, np.array(ids)

print("Training faces... Please wait.")
faces, ids = get_images_and_labels()
recognizer.train(faces, ids)
recognizer.write(trainer_path)

print("Model trained successfully. Ready for authentication.")
