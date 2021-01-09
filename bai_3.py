# nhận diện khuông mặt, vẽ hình chữ nhật màu Green quanh khuông mặt.
# đếm số khuôn mặt có trong ảnh
# nếu nhấn 'S' thì lưu khuôn mặt ra file ảnh 0.png, 1.png,...(tùy số lượng)
import cv2 as cv

# load thư viện
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# hàm lưu khuôn mặt
def save_face(frame, faces):
    i = 0
    for (x, y, w, h) in faces:
        crop = frame[y: y + h, x: x + w]
        cv.imwrite("file{}.png".format(i), crop)
        i = i + 1
    return

camera = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, frame = camera.read()

    if ret:
        # chuyển sang gray
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame_gray, 1.2, 10, minSize=(100, 100))

        for (x, y, w, h) in faces:
            # vẽ hình chữ nhật
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_color = frame[y: y + h, x: x + w]

        cv.imshow("FRAME", frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            save_face(frame, faces)

camera.release()
cv.destroyAllWindows()
