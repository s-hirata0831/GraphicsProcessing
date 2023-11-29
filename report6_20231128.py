import cv2

#画像読み込み
img = cv2.imread(R"C:\Users\hirat\Documents\OpenCV\Picture\lena_std.bmp")
original = cv2.imread(R"C:\Users\hirat\Documents\OpenCV\Picture\lena_std.bmp")
original[:, :, (0,1)] = 0
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#thresholdは返り値を2つもつが，今回は一つだけでいいのでアンダーバーを適用する。
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Color', img)
cv2.imshow('Gray', gray)
cv2.imshow('Binray', binary)
cv2.imshow('Original', original)

cv2.waitKey(0)
cv2.destroyAllWindows()