import cv2
import datetime

# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
attendance = set()  # To avoid duplicate entries

print("Attendance System Started... Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, 
                                          minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        # Add simple label
        cv2.putText(frame, "Present", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Log attendance
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        name = f"Student_{len(attendance)+1}"
        
        if name not in attendance:
            attendance.add(name)
            print(f"✅ Attendance Marked: {name} at {timestamp}")

    # Show attendance count
    cv2.putText(frame, f"Present: {len(attendance)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Live Face Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("\nFinal Attendance:", attendance)