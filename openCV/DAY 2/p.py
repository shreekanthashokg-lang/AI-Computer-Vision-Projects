import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\shreekanth\OneDrive\Desktop\openCV\DAY 2\shreekanth photo.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Advanced Techniques

# 1. Color Masking (Remove/Keep specific color)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0, 50, 50])
upper = np.array([30, 255, 255])
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

# 2. Edge Enhancement
edges = cv2.Canny(gray, 50, 150)
enhanced = cv2.addWeighted(gray, 1, edges, 0.5, 0)

# 3. Perspective Transformation (Warp)
pts1 = np.float32([[50,50], [400,50], [50,300], [400,300]])
pts2 = np.float32([[0,0], [300,0], [0,300], [300,300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(img, M, (300, 300))

# 4. Image Pyramid
pyr_down = cv2.pyrDown(img)
pyr_up = cv2.pyrUp(pyr_down)

# 5. Custom Kernel (Sharpening)
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpened = cv2.filter2D(gray, -1, kernel)

print("All advanced operations completed!")