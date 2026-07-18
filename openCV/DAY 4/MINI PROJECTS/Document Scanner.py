import cv2
import numpy as np

img = cv2.imread('shreekanth photo.jpeg')   # Replace with document photo

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 150)

# Find contours
contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

for cnt in contours:
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    if len(approx) == 4:   # Quadrilateral found
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
        break

cv2.imshow('Document Scanner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()