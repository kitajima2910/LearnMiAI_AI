import cv2 as cv

# thư việt giúp rotate ảnh
import imutils


# đọc ảnh
image = cv.imread("sample.jpg")

# resize ảnh
image_rs = cv.resize(image, None, fy=0.2, fx=0.2)

# xoay ảnh 90 độ
image_rotate = imutils.rotate(image_rs, 90)
cv.imshow("Anh rotate", image_rotate)

# xoay ảnh 45 độ
image_rotate = imutils.rotate(image_rs, 45)
cv.imshow("Anh rotate", image_rotate)

# dừng màn hình
cv.waitKey()

# đóng tất cả các cửa sổ
cv.destroyAllWindows()
