import cv2

# đọc ảnh
image = cv2.imread("sample01.jpg")
cv2.waitKey()

# đọc ảnh xám
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# hiển thị ảnh
cv2.imshow("Anh xam", image_gray)
cv2.waitKey()

# muốn threshold binary: (BRG -> GRAY -> chọn ngưỡng -> duyệt các điểm ảnh)
# điểm ảnh > ngưởng threshold là 255, ngược lại là 0 => (0, 1)
ret, threshold_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# hiển thị ảnh
cv2.imshow("Anh binary", threshold_binary)
cv2.waitKey()

# xử lý khi chưa biết chọn ngưỡng như nào
adaptive_threshold = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# hiển thị ảnh
cv2.imshow("Anh binary", adaptive_threshold)
cv2.waitKey()

# đóng tất cả các cửa sổ
cv2.destroyAllWindows()
