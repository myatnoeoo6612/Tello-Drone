from djitellopy import Tello
import time
import cv2

# Initialize the Tello drone
tello = Tello()
tello.connect()

tello.streamoff()
tello.streamon()
cap = cv2.VideoCapture('udp//0.0.0.0:11111')

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("Tello Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
tello.streamoff()