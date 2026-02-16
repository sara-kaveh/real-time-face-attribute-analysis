import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')

def detect_faces(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100,100))

    return faces

def analyze_face(frame, face_coords):

    x, y, w, h = face_coords
    face_img = frame[y:y+h, x:x+w]

    if face_img.size == 0:
        return None

    face_img = cv2.resize(face_img, (150, 150))

    try:

        result = DeepFace.analyze(face_img, actions=['emotion','age','gender','race'], enforce_detection=False, silent=True, detector_backend='opencv')

        if isinstance(result, list):
            result = result[0]

        return result

    except Exception as e:

        return None
