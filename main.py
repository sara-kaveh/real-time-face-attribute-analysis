import cv2
from camera import start_camera, get_frame, release_camera
from analyzer import detect_faces, analyze_face
from utils import draw_results

cap = start_camera()
frame_count = 0
face_results = {} 

while True:

    ret, frame = get_frame(cap)
    if not ret:
        break

    frame_count += 1
    small_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    faces = detect_faces(small_frame)

    for i, (x, y, w, h) in enumerate(faces):

        x = int(x*2)
        y = int(y*2)
        w = int(w*2)
        h = int(h*2)

        face = (x,y,w,h)

        # analyze every 10 frames
        if frame_count % 10 == 0:

            face_results[i] = analyze_face(frame, face)

        result = face_results.get(i)

        frame = draw_results(frame, face, result)

    cv2.imshow("Face Analysis", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

release_camera(cap)
