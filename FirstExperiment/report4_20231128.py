import cv2

#画像読み込み
img = cv2.imread(R"C:\Users\hirat\Documents\OpenCV\Picture\lena_std.bmp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Color', img)
cv2.imshow('Gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()