from djitellopy import Tello
import time, cv2
from threading import Thread

# Create and connect to the Tello drone
tello = Tello()
tello.connect()

# Get and print battery level
power = tello.get_battery()
print("Power Level =", power, "%")

# Enable mission pads and set detection direction
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(2)

# Initialize video streaming and recording
keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # Create a VideoWriter object, recording to video.avi
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video2.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# Run the recorder in a separate thread to prevent blocking
recorder = Thread(target=videoRecorder)
recorder.start()

# Take off and start mission pad detection
tello.takeoff()

pad = tello.get_mission_pad_id()

# Detect and react to pads until pad #1 is detected
while pad != 1:
    if pad == 3:
        cv2.imwrite("picture3.png", frame_read.frame)
        tello.move_left(60)
        tello.move_right(60)
        print("Detected pad 3")

    if pad == 7:
        cv2.imwrite("picture7.png", frame_read.frame)
        tello.rotate_counter_clockwise(90)
        tello.rotate_clockwise(90)
        print("Detected pad 7")

    if pad == 8:
        cv2.imwrite("picture8.png", frame_read.frame)
        tello.move_down(30)
        tello.move_up(30)
        print("Detected pad 8")

    if pad == 4:
        cv2.imwrite("picture4.png", frame_read.frame)
        tello.land()
        print("Detected pad 4 - Landing")
        break

    pad = tello.get_mission_pad_id()

# Get and print battery level again
power = tello.get_battery()
print("Power Level =", power, "%")

# Stop mission pad detection and land the drone
tello.disable_mission_pads()
tello.land()

# Get and print flight time
ft = tello.get_flight_time()
print("Flight Time =", ft)

# Terminate video recording
keepRecording = False
recorder.join()

# End the Tello connection
tello.end()
