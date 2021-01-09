import cv2

# mở camera
# đọc file video
camera_id = "sample.avi"
# id = 0 là camera default
camera_id = 0
cap = cv2.VideoCapture(camera_id)

# đọc ảnh từ camera
while True:
    # đọc từng frame ảnh từ camera và trả về 2 tham số (true, ảnh)
    ret, frame = cap.read()

    # hiển thị ảnh
    cv2.imshow("Cam", frame)

    # điều kiện dừng nếu bấm q thì thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# giải phóng camera
cap.release()
# đóng các cửa sở
cv2.destroyAllWindows()
