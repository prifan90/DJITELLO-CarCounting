import cv2
import torch
import numpy as np
from djitellopy import tello
import KeyPressModule as kp
from time import sleep

path = 'D:/Kuliah/D4 TRIK/SEMESTER 3/Robotika/DJITello/Parking Space Counter/Vehicle/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path, force_reload=True)

def detect_cars(frame):
    car_count = 0
    results = model(frame)
    frame = np.squeeze(results.render())
    labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
    n = len(labels)
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    for i in range(n):
        row = cord[i]
        if row[4] >= 0.30:
            x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(row[3] * y_shape)
            car_count +=1
    return car_count, frame

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed
    if kp.getKey("q"):
        me.land()
        sleep(3)
    if kp.getKey("e"):
        me.takeoff()
    return [lr, fb, ud, yv]

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

# cap = cv2.VideoCapture('Car.mp4')
while True:
    frame = me.get_frame_read().frame
    # ret, frame = cap.read()
    frame = cv2.resize(frame, (480,360))
    car_count, frame = detect_cars(frame)
    cv2.putText(frame, "Jumlah Mobil : "+str(car_count), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,0), 3)
    cv2.imshow("Cars Detection", frame)
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)
    cv2.waitKey(1)