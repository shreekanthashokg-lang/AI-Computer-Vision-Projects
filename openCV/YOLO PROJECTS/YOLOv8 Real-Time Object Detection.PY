# First install if not already installed:
# pip install ultralytics opencv-python

import cv2
from ultralytics import YOLO
import time

# Load YOLOv8 model (nano version - fast for real-time)
model = YOLO('yolov8n.pt')   # You can also use yolov8s.pt for better accuracy

cap = cv2.VideoCapture(0)    # 0 = webcam

print("YOLO Real-Time Object Detection Started!")
print("Press 'q' to quit.")

while True:
    start_time = time.time()
    
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame, verbose=False)

    # Draw results on frame
    annotated_frame = results[0].plot()   # This draws boxes, labels, confidence

    # Calculate FPS
    fps = 1 / (time.time() - start_time)
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('YOLOv8 Real-Time Object Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()