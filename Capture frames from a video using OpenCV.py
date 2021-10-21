#!/usr/bin/env python
# coding: utf-8
#pip install opencv-python

import cv2
import datetime

vidcap = cv2.VideoCapture('C:/Users/4akhi/Desktop/big_buck_bunny_720p_5mb.mp4')

frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = int(vidcap.get(cv2.CAP_PROP_FPS))

seconds = int(frames / fps)
print("duration in seconds:", seconds)

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("C:/Users/4akhi/Desktop/sample/"+str(sec)+" sec.webp", image)     # save frame as PNG file
    return hasFrames
sec = 1
frameRate = seconds * 0.25 #it will capture image in each (seconds * 0.25) second
print(frameRate)
success = getFrame(sec)
while success:
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)