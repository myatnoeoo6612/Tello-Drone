#Simply import of "panoramaModule.py" and you can use each function by calling it with name of the drone inside arguments.
from djitellopy import Tello
import time




tello = Tello()
tello.connect()

print(tello.get_battery())

tello.takeoff()
tello.move_up(20)
time.sleep(1)
print(tello.get_battery())
time.sleep(1)
print(tello.get_battery())


tello.land()
