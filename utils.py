import cv2

def draw_results(frame, face_coords, result):

    x, y, w, h = face_coords

    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    if result is None:
        return frame

    emotion = result["dominant_emotion"]
    age = result["age"]
    gender = result["dominant_gender"]
    race = result["dominant_race"]

    text = f"{emotion} | {gender} | {age} | {race}"

    cv2.putText(frame, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    return frame