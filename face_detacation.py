# import face_recognition
# import cv2
# import os
# import pickle

# # Directory to store known faces and encodings
# KNOWN_FACES_DIR = "known_faces"
# os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

# # Load or create database
# face_data = {}

# def encode_face(image_path, name):
#     image = face_recognition.load_image_file(image_path)
#     encodings = face_recognition.face_encodings(image)
#     if encodings:
#         face_data[name] = encodings[0]  # Save the first encoding

# # Encode a sample face
# encode_face("john_doe.jpg", "John Doe")

# # Save encodings to file
# with open("face_data.pkl", "wb") as f:
#     pickle.dump(face_data, f)
