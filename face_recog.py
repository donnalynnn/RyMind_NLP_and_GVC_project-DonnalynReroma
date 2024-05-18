import face_recognition
import cv2
import os
import glob
import numpy as np

class FaceRecognition:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
  
        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
         # Print the current working directory
        print("Current working directory:", os.getcwd())
        
        # Print the absolute path of the images directory
        abs_images_path = os.path.abspath(images_path)
    
        print("Absolute path of images directory:", abs_images_path)
        
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))

        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            
            # Check if the image is loaded successfully
            if img is None:
                print(f"Failed to load image {img_path}.")
                continue
            
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            
            # Get face encodings
            face_encodings = face_recognition.face_encodings(rgb_img)
            
            # Check if any face encodings were found
            if len(face_encodings) > 0:
                img_encoding = face_encodings[0]

                # Get the filename only from the initial file path.
                basename = os.path.basename(img_path)
                (filename, ext) = os.path.splitext(basename)

                # Store file name and file encoding
                self.known_face_encodings.append(img_encoding)
                self.known_face_names.append(filename)
            else:
                print(f"No faces detected in image {img_path}.")

        print("Encoding images loaded")

    
    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Check if any faces were detected
            if len(face_encodings) > 0:
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                # Correctly check if face_distances is not empty
                if face_distances.size > 0:
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                else:
                    print("No face distances available.")
            else:
                print("No faces detected in the frame.")

            face_names.append(name)

        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names