import pytesseract as pt
import PIL.Image
import cv2
import capture_img

def trim_num(text):
    res=""
    for i in range(len(text)):
        if text[i].isnumeric()==True:
            res+=text[i]
    return res


def image():
    my_config=r"--psm 11 --oem 3"
    capture_img.capture()
    text = pt.image_to_string(PIL.Image.open("img.jpg"), config=my_config)
    return trim_num(text)

if __name__=='__main__':
    image()
    print(image())
