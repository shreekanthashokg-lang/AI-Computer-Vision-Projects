import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load your image
img = cv2.imread(r"C:\Users\shreekanth\OneDrive\Desktop\openCV\DAY 1\Shreekanth.jpeg")



if img is None:
    print("Error: Image not found!")
else:
    print("✅ Image loaded! Shape:", img.shape)

    # ================== BASIC OPERATIONS ==================
    
    # 1. Resize
    resized = cv2.resize(img, (600, 500))   # width, height
    cv2.imwrite('resized.jpg', resized)

    # 2. Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Gaussian Blur (Smoothing)
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite('blurred.jpg', blurred)

    # 4. Edge Detection (Canny)
    edges = cv2.Canny(gray, 100, 200)

    # 5. Drawing on Image (Rectangle, Circle, Text)
    img_draw = img.copy()
    cv2.rectangle(img_draw, (100, 100), (400, 400), (0, 255, 0), 5)      # Green rectangle
    cv2.circle(img_draw, (300, 250), 80, (0, 0, 255), 5)                 # Red circle
    cv2.putText(img_draw, 'Shreekanth', (150, 600), cv2.FONT_HERSHEY_SIMPLEX, 
                2, (255, 0, 0), 5, cv2.LINE_AA)                           # Blue text

    # ================== DISPLAY ALL ==================
    titles = ['Original', 'Grayscale', 'Blurred', 'Edges', 'Drawing']
    images = [cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 
              gray, 
              cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB),
              edges, 
              cv2.cvtColor(img_draw, cv2.COLOR_BGR2RGB)]

    plt.figure(figsize=(15, 10))
    for i in range(5):
        plt.subplot(2, 3, i+1)
        if i == 1 or i == 3:   # grayscale & edges
            plt.imshow(images[i], cmap='gray')
        else:
            plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()

    # Save all results
    cv2.imwrite('edges.jpg', edges)
    cv2.imwrite('drawing.jpg', img_draw)

    print("✅ All images saved successfully!")