import cv2
import imutils

# đọc ảnh
image = cv2.imread('bongbong.png')

# chuyển ra màu xám
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# mã hóa nhị phân
thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                              cv2.THRESH_BINARY_INV, 21, 10)

contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=False)

number = 0

# loop over our contours
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    print(x, y, w, h)
    if (85 < w < 150) and (100 < h < 150):
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number += 1

print("Number of Contours found = " + str(number))

cv2.imshow('Pix', image)
cv2.waitKey()
cv2.destroyAllWindows()
