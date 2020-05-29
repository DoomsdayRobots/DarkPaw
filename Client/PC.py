#!/user/bin/python3
# file name    : PC.py
# Author       : David Metcalf
# Date         : 2020/5/28
# this is run on yoyr lap top desk top computer.

import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.PAIR)
footage_socket.bind('tcp://*:5555')

while True:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        nping = np.frombuffer(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("stream", source)
        cv2.waitKey(1)
