import cv2
import numpy as np
import matplotlib.pyplot as plt

# Correct file name from your folder
img = cv2.imread('shreekanth photo.jpeg')

if img is None:
    print("Error: Image not found! Check the filename and path.")
else:
    print("✅ Image loaded successfully!")
    print("Image Shape:", img.shape)   # (height, width, channels)

    # Convert BGR (OpenCV default) to RGB for correct colors
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Display original image
    plt.figure(figsize=(10, 8))
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis('off')
    plt.show()

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.figure(figsize=(10, 8))
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')
    plt.show()

    # Optional: Save the grayscale image
    cv2.imwrite('grayscale_output.jpg', gray)
    print("Grayscale image saved as 'grayscale_output.jpg'")






    # Resize image
resized = cv2.resize(img, (500, 400))  # width, height
cv2.imwrite('resized.jpg', resized)

# Blur the image
blurred = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite('blurred.jpg', blurred)

print("Additional images saved!")