from djitellopy import Tello

# create and connect
tello = Tello()
tello.connect()

# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(1)  # forward detection only  只识别前方

tello.takeoff()

pad = tello.get_mission_pad_id()

# detect and react to pads until we see pad #1

while pad != 1:
    
    if pad == 5:
        tello.move_up(50)   
        tello.rotate_clockwise(180)

    if pad == 8:
        tello.move_up(50)
        tello.flip_forward()

    pad = tello.get_mission_pad_id()

# graceful termination
# 安全结束程序
tello.disable_mission_pads()
tello.land()
tello.end()
