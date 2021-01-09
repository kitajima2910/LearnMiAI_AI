import cv2

image = cv2.imread("bongbong.png")

cv2.imshow("Anh", image)
cv2.waitKey()

# chuyển ảnh xám thành ảnh grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# nhị phân hóa ảnh
thresh = cv2.Canny(image_gray, 127, 255)
# image_adaptive_threshold = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                                  cv2.THRESH_BINARY, 11, 2)

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# vẽ lại ảnh contour vào ảnh gốc
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imshow("Anh contours", image)
cv2.waitKey()

cv2.destroyAllWindows()
