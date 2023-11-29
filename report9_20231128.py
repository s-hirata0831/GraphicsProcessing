import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    cv2.imshow('CaptureImage', frame)

    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()