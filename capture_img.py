import cv2


def capture():
    cap = cv2.VideoCapture(0)
    cap.set(3,640) #width=640
    cap.set(4,480) #height=480

    if cap.isOpened():
        _,frame = cap.read()
        cap.release() #releasing camera immediately after capturing picture
        if _ and frame is not None:
            cv2.imwrite('img.jpg', frame)