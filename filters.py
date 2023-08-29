import cv2
import numpy as np

# Load an image
image = cv2.imread(r'C:\xampp\htdocs\Intelligent_counter\ai_project\counter_5.jpg')

# Convert the image to grayscale (if needed)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Sobel edge detection
sobel_x = cv2.Sobel(blurred_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blurred_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)

# Apply Canny edge detection
canny_edges = cv2.Canny(blurred_image, threshold1=30, threshold2=70)

# Display the original and filtered images
# cv2.imwrite('Original Image', image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.imshow('Sobel Edges', sobel_edges)
# cv2.imshow('Canny Edges', canny_edges)

#write new files
cv2.imwrite('blurred.jpg', blurred_image)
cv2.imwrite('sobel_edges.jpg',sobel_edges )

