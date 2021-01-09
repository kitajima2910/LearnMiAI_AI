# đọc ảnh từ camera và chuyển sang màu xám, hiển thị lên màn hình
import cv2

# khai báo đối tượng video
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# đọc ảnh từ camera
while True:
    ret, frame = cap.read()

    if ret:
        # convert ảnh đọc sang ảnh xám
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # hiển thị ảnh
        cv2.imshow("Frame", frame_gray)

    # điều kiện dừng
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# giải phóng video
cap.release()

# đóng tất cả các cửa sở
cv2.destroyAllWindows()
