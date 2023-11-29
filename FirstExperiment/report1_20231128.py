import cv2

#画像読み込み
img = cv2.imread(R"/Users/hiratasoma/Documents/GraphicsProcessing/Picture/lena_std.bmp")
cv2.imshow('img1', img)

cv2.waitKey(0)
cv2.destroyAllWindows()