import cv2 as cv
import time
import numpy as np
import module as md
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam,hCam = 1280 , 720

cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = md.handDetector()



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]




while True:
    success,frm = cap.read()
    frm = cv.flip(frm, 1)
    frm = detector.findHands(frm)
    lmList = detector.findPosition(frm)
    if len(lmList)!=0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv.circle(frm,(x1,y1),10,(255,0,255),cv.FILLED)
        cv.circle(frm, (x2, y2), 10, (255, 0, 255), cv.FILLED)
        cv.line(frm,(x1,y1),(x2,y2),(255,0,255),3)
        cv.circle(frm, (cx, cy), 10, (255, 0, 255), cv.FILLED)
        length = math.hypot(x2 - x1, y2 - y1)


        vol = np.interp(length,[45,200],[minVol,maxVol])
        volume.SetMasterVolumeLevel(vol, None)
        print(int(length),vol)


        if length <= 50:
            cv.circle(frm, (cx, cy), 10, (0, 255, 0), cv.FILLED)



        cv.imshow("Image", frm)
        cv.waitKey(1)