import easyocr

import cv2
import numpy as np

def trimming_num(text):
    res=""
    for i in range(len(text)):
        if text[i].isnumeric()==True:
            res+=text[i]
    return res


# Load an image
image = cv2.imread(r'C:\xampp\htdocs\Intelligent_counter\ai_project\dataset_train\counter_12.png')

# Convert the image to grayscale (if needed)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Sobel edge detection


# Apply Canny edge detection
canny_edges = cv2.Canny(blurred_image, threshold1=30, threshold2=70)
laplacian = cv2.Laplacian(image,cv2.CV_64F)
sobel_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)
# Display the original and filtered images
# cv2.imwrite('Original Image', image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.imshow('Sobel Edges', sobel_edges)
# cv2.imshow('Canny Edges', canny_edges)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#write new files
cv2.imwrite('blurred.jpg', gray)


filename = r"C:\xampp\htdocs\Intelligent_counter\ai_project\img.jpg"



reader=easyocr.Reader(['en'])
results=reader.readtext(filename)
for result in results:
    text=result[1].strip()
    res=trimming_num(text)
    print(res)


