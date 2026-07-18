import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\shreekanth\OneDrive\Desktop\openCV\DAY 2\shreekanth photo.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Different Thresholding
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 2. Adaptive Thresholding
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                 cv2.THRESH_BINARY, 11, 2)

# 3. Noise Removal
blur = cv2.GaussianBlur(gray, (5,5), 0)
median = cv2.medianBlur(gray, 5)
bilateral = cv2.bilateralFilter(gray, 9, 75, 75)

# 4. Morphological Operations
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# 5. Histogram Equalization
equalized = cv2.equalizeHist(gray)

# 6. Rotation
(h, w) = gray.shape
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)   # 45 degrees
rotated = cv2.warpAffine(gray, M, (w, h))

# Display (you can expand this)
plt.figure(figsize=(15, 12))
titles = ['Original', 'Binary', 'Otsu', 'Adaptive', 'Equalized', 'Rotated']
images = [gray, binary, otsu, adaptive, equalized, rotated]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.show()