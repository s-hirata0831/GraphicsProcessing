import cv2

#画像読み込み
img = cv2.imread(R"C:\Users\hirat\Documents\OpenCV\Picture\lena_std.bmp")
cv2.imshow('img1', img)
cv2.imshow('img2', img)

cv2.waitKey(0)
cv2.destroyAllWindows()