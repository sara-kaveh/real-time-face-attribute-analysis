import cv2

def start_camera():
    cap = cv2.VideoCapture(0)
    return cap

def get_frame(cap):
    ret, frame = cap.read()
    return ret, frame

def release_camera(cap):
    cap.release()
    cv2.destroyAllWindows()
