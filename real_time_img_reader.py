import pytesseract as pt
import PIL.Image
import cv2
import time
def image(frame):
    my_config=r"--psm 11 --oem 3"

    text = pt.image_to_string(PIL.Image.open(frame), config=my_config)
    return text

def image_reader():
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        cv2.imshow("Streaming....", frame)
        if cv2.waitKey(1)==ord('q'):
            cv2.imwrite('captured_frame.jpg', frame)
            filename='captured_frame.png'
            text=image(filename)
            print(text)
            break
    cap.release()
    cv2.destroyAllWindows()

image_reader()
    