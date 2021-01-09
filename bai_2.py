# đọc ảnh tử file video, hiển thị lên màn hình. nhấn A quay ngược 90, nhấn B quay theo chiều.
import cv2
import imutils

# khai báo đối tượng
video_src = "video.mp4"
cap = cv2.VideoCapture(video_src)

# rotate default
rotate = 0

while True:
    ret, frame = cap.read()

    if ret:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)
        cv2.imshow("FRAME", frame)

    # điều kiện xử lý
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        rotate = 90
    elif key == ord('d'):
        rotate = -90

# giải phóng các frame
cap.release()

# đóng tất cả các cửa sổ
cv2.destroyAllWindows()