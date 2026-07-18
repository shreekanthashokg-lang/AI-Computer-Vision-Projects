import cv2

def apply_filter(frame, filter_type):
    if filter_type == 1:   # Grayscale
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 2: # Blur
        return cv2.GaussianBlur(frame, (25, 25), 0)
    elif filter_type == 3: # Edge
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 50, 150)
    elif filter_type == 4: # Sharpen
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        return cv2.filter2D(frame, -1, kernel)
    return frame

cap = cv2.VideoCapture(0)
filter_type = 0

print("Press 1:Grayscale | 2:Blur | 3:Edge | 4:Sharpen | q:Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if filter_type != 0:
        processed = apply_filter(frame, filter_type)
        if len(processed.shape) == 2:  # grayscale/edge
            processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
        cv2.imshow('Filter App', processed)
    else:
        cv2.imshow('Filter App', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('1'):
        filter_type = 1
    elif key == ord('2'):
        filter_type = 2
    elif key == ord('3'):
        filter_type = 3
    elif key == ord('4'):
        filter_type = 4
    elif key == ord('0'):
        filter_type = 0

cap.release()
cv2.destroyAllWindows()