import cv2

# đọc ảnh
image = cv2.imread("sample01.jpg")

# đọc ảnh xám
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Anh xam", image_gray)
cv2.waitKey()

# adaptive threshold
# image_adaptive_threshold = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                                  cv2.THRESH_BINARY, 11, 2)

# tìm cạnh, viền hàm cv2.Canny điền 2 ngưỡng cho hợp lý, áp dụng vào bài toán tìm
image_edge = cv2.Canny(image_gray, threshold1=100, threshold2=200)
cv2.imshow("Anh edge", image_edge)
cv2.waitKey()

# đóng tất cả cửa sổ
cv2.destroyAllWindows()
