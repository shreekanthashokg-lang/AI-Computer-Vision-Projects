import cv2
import numpy as np

img = cv2.imread(r"C:\Users\shreekanth\OneDrive\Desktop\openCV\Mini Project\shreekanth photo.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 1: Blur + Edge Detection
blurred = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blurred, 50, 150)

# Step 2: Morphological Operations
kernel = np.ones((5,5), np.uint8)
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Step 3: Find Contours (Biggest rectangle)
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

# Draw contour
cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imwrite('scanned_output.jpg', img)
print("Mini Project Completed!")