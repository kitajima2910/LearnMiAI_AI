import cv2

# đọc ảnh
image = cv2.imread("sample.jpg")

# hiển thị ảnh
cv2.imshow("Anh mau", image)

# dừng màn hình
cv2.waitKey()

# convert ảnh
# hệ màu trong OpenCV là BGR
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Anh gray", image_gray)
cv2.waitKey()

# convert ảnh
# hệ màu HSV làm giảm bớt sự ảnh hưởng của ánh sáng dễ xử lý ảnh
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Anh hsv", image_hsv)
cv2.waitKey()

# đóng các cửa sổ
cv2.destroyAllWindows()

