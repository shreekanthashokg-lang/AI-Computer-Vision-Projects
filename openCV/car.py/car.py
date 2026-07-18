import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load your image
img = cv2.imread(r"C:\Users\shreekanth\OneDrive\Desktop\openCV\car.py\car.jpeg")
  

if img is None:
    print("Error: Image not found!")
else:
    print("✅ Image Loaded! Shape:", img.shape)

# ====================== ALL TOPICS ======================

# 1. Image Color Conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 2. Resizing an Image
resized = cv2.resize(img, (600, 400))        # (width, height)

# 3. Flipping an Image
flip_horizontal = cv2.flip(img, 1)   # 1 = horizontal
flip_vertical = cv2.flip(img, 0)     # 0 = vertical
flip_both = cv2.flip(img, -1)        # -1 = both

# 4. Cropping
# Format: img[y_start:y_end, x_start:x_end]
cropped = img[100:400, 150:450]      # Adjust numbers as per your image

# 5. Translation (Shifting + Slanting)
# Shifting
M_shift = np.float32([[1, 0, 100], [0,1 , 50]])   # Shift 100 right, 50 down
translated = cv2.warpAffine(img, M_shift, (img.shape[1], img.shape[0]))

# 6. Rotating
(h, w) = img.shape[:2]
center = (w//2, h//2)
M_rotate = cv2.getRotationMatrix2D(center, 45, 1.0)   # 45 degrees
rotated = cv2.warpAffine(img, M_rotate, (w, h))

# ====================== DISPLAY ALL ======================
plt.figure(figsize=(15, 12))

titles = ['1. Original', '1. Grayscale', '2. Resized', 
          '3. Flip Horizontal', '4. Cropped', '5. Translated',
          '6. Rotated']

images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), gray, 
          cv2.cvtColor(resized, cv2.COLOR_BGR2RGB),
          cv2.cvtColor(flip_horizontal, cv2.COLOR_BGR2RGB),
          cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB),
          cv2.cvtColor(translated, cv2.COLOR_BGR2RGB),
          cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)]

for i in range(7):
    plt.subplot(3, 3, i+1)
    if i == 1:  # Grayscale
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()

print("✅ All Image Processing Techniques Completed!")