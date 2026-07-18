import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Create a blank mask same size as frame
    mask = np.zeros_like(frame)

    # Draw a white filled rectangle on the mask
    cv2.rectangle(mask, (100, 100), (400, 400), (255, 255, 255), -1)

    # Apply bitwise AND to keep only the region inside the rectangle
    masked_frame = cv2.bitwise_and(frame, mask)

    # Show original and masked video
    cv2.imshow("Original", frame)
    cv2.imshow("Masked", masked_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
