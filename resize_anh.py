import cv2

# đọc ảnh
image = cv2.imread("sample.jpg")

# resize ảnh tuyệt đối 500, 500
image_rs = cv2.resize(image, dsize=(500, 500))

# resize ảnh tương đối, giảm 1 nửa
image_rs = cv2.resize(image, None, fx=0.5, fy=0.5)

# resize ảnh tương đối, gấp đôi
image_rs = cv2.resize(image, None, fx=2, fy=2)

# hiển thị ảnh
cv2.imshow("Anh rs", image_rs)

# dừng màn hình
cv2.waitKey()

# đóng tất cả cửa sổ
cv2.destroyAllWindows()