from djitellopy import Tello
import time
import cv2

# Initialize the Tello drone
tello = Tello()
tello.connect()

# Start video stream
tello.streamon()
time.sleep(2)  # Allow time for the stream to initialize

# Try grabbing a single frame
frame_read = tello.get_frame_read()
frame = frame_read.frame

# Display the frame
if frame is not None:
    cv2.imshow("Tello Video Stream", frame)
    cv2.waitKey(0)  # Press any key to close the window
else:
    print("Failed to retrieve a frame.")

# Clean up
tello.streamoff()
cv2.destroyAllWindows()
