import cv2

# đọc ảnh
image = cv2.imread("sample01.jpg")

# làm mờ ảnh blur, ksize là 2 số lẻm càng lớn ảnh càng mờ
blur = cv2.GaussianBlur(image, ksize=(31,25), sigmaX=0)
cv2.imshow("Anh blur", blur)
cv2.waitKey()

# đóng tất cả cửa sổ
cv2.destroyAllWindows()