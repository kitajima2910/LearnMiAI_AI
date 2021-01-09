import cv2

# đọc ảnh
image = cv2.imread("sample.jpg")
# đọc ảnh trắng đen
image = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

# hiển thị ảnh
cv2.imshow("Anh", image)

# chỉnh kích thước màn hình
cv2.resizeWindow("Anh", 1000, 700)

# dừng màn hình
cv2.waitKey()

# đóng các cửa sổ
cv2.destroyAllWindows()
