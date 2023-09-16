import cv2
import matplotlib.pyplot as plt
import cvlib as cv
import urllib.request
import numpy as np
from cvlib.object_detection import draw_bbox

url='http://192.168.209.19/cam-hi.jpg'
im=None
 
def capture():
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    im = cv2.imdecode(imgnp,-1)
    cv2.imwrite('img_esp.png',im)
    return 'img_esp.png'

if __name__ == '__main__':
    capture()