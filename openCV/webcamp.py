import cv2
cap = cv2.VideoCapture(0)

# Ensure the classifier is loaded correctly here too
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Haar Cascade requires grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    
    for (x, y, w, h) in faces:
        # Isolate the face
        face_crop = frame[y:y+h, x:x+w]
        
        # Format the face crop for your CNN model
        img_input = cv2.resize(face_crop, (64, 64))
        img_input = img_input / 255.0
        img_input = np.reshape(img_input, (1, 64, 64, 3))
        
        # Predict mask presence
        prediction = model.predict(img_input, verbose=0)
        raw_score = prediction[0][0]
        
        if raw_score > 0.5:
            label = "No Mask"
            confidence = raw_score * 100
            color = (0, 0, 255)  # Red box
        else:
            label = "Mask"
            confidence = (1 - raw_score) * 100
            color = (0, 255, 0)  # Green box
            
        text = f"{label}: {confidence:.2f}%"
        
        # Draw target geometry on real-time frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    
    cv2.imshow("Real-Time Face Mask Detection", frame)
    
    # Press 'q' to break the video loop safely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()