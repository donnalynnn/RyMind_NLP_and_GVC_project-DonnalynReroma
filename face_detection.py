import cv2
from face_recog import FaceRecognition

class FaceDetection:
    def __init__(self):
        self.sfr = FaceRecognition()
        self.sfr.load_encoding_images("images/")
        self.cap = cv2.VideoCapture(0) #change value 0 if you have secondary camera
        if not self.cap.isOpened():
            print("Error opening video source")
            exit()
        self.last_detected_name = None

    def while_true(self):
        while True:
            ret, frame = self.cap.read()

            # Detect Faces
            face_locations, face_names = self.sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                self.last_detected_name = name

                cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            cv2.imshow("RyMind", frame)

            key = cv2.waitKey(1)
            if key == 27:
                break

    def get_name(self):
        return self.last_detected_name

    def run(self):
        self.while_true()
        self.cap.release()
        cv2.destroyAllWindows()


# pip install face_recognition
# pip3 install --upgrade pip
# pip install --upgrade setuptools wheel
