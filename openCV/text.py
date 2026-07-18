import cv2

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Add text overlay
    text = "Hello Shreekanth. Welcome to Computer Vision!"
    cv2.putText(
        frame, 
        text, 
        (50, 50),                # Position (x, y)
        cv2.FONT_HERSHEY_SIMPLEX, # Font
        1,                        # Font scale
        (0, 255, 0),              # Color (B, G, R) → Green
        2,                        # Thickness
        cv2.LINE_AA               # Line type
    )

    cv2.imshow("Webcam", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
