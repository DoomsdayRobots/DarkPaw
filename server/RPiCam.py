#!/user/bin/python3
# file name    : RPiCam.py
# Author       : David Metcalf
# Date         : 2020/5/28
# this is run on the raspberry pi3 B or B+

import cv2
import zmq
import base64
import picamera
from picamera.array import PiRGBArray

IP = '192.168.0.25'

camera = picamera.PiCamera()
camera.resolution = (64,480)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(640, 480))

context = zmq.Context()
footage_socket = context.socket(zmq,PAIR)
footage_socket.connection('tcp://%s:5555'%IP)
print(IP)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame_image = frame.array        
        encoded, buffer = cv2.imencode('.jpg', frame_image)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)
        rawCapture.truncate(0)
