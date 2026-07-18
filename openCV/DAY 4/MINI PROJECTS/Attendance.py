import cv2
import numpy as np
import datetime

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
recognized_names = {}  # Simple dictionary for demo

print("Press 'q' to quit | Press 's' to mark attendance")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
        # Simple "recognition" demo (you can improve with actual embedding later)
        name = "Student"
        if (x, y) not in recognized_names:
            recognized_names[(x, y)] = name
        
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.9, (0, 255, 0), 2)
        
        # Mark attendance on 's' key
        if cv2.waitKey(1) & 0xFF == ord('s'):
            with open("attendance.txt", "a") as f:
                f.write(f"{name} - {datetime.datetime.now()}\n")
            print(f"Attendance marked for {name}")

    cv2.imshow('Smart Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()