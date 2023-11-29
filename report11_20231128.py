import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('CaptureImage', frame)
    cv2.imshow('BinaryCapture', binary)

    key = cv2.waitKey(10)
    if key == ord('s'):
        cv2.imwrite(R"C:\Users\hirat\Documents\OpenCV\Picture\camera_binary.bmp", binary)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

#画像保存
cv2.imwrite(R"C:\Users\hirat\Documents\OpenCV\Picture\lena_gray.bmp", gray)