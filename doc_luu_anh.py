import cv2

# đọc ảnh chế độ màu xám
image = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)
# lưu ảnh
cv2.imwrite("sample_gray.jpg", image)