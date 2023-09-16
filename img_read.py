import pytesseract as pt
import PIL.Image
import cv2
import esp_get
import numpy as np
import easyocr
import cleanser

def trim_num(text):
    res=""
    for i in range(len(text)):
        if text[i].isnumeric()==True:
            res+=text[i]
    return res

def easy_ocr(filename):
    reader=easyocr.Reader(['en'])
    results=reader.readtext(filename)
    for result in results:
        text=result[1].strip()
        res=trim_num(text)
    return res

def image():
    my_config=r"--psm 11"
    image = cv2.imread(esp_get.capture(), 0)
    
    sat=cv2.addWeighted(image, 1, np.zeros(image.shape, image.dtype), 0, 1)
    thresh = cv2.threshold(sat, 127, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cv2.imwrite('img.jpg',thresh)
    text = easy_ocr('img.jpg')
    print(text)
    return cleanser.cleanse(text)

if __name__=='__main__':
    print(image())
