import cv2
# from cvzone.HandTrackingModule import HandDetector
import handtrackingmodule
from time import sleep
# import numpy as np
# import cvzone
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)



detector=handtrackingmodule.handDetector()
# detector2=htm2.handDetector()

keys=[["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L",";"],
        ["Z","x","C","V","B","N","M",",",".","/"]]

finalText = ""  

keyboard = Controller()


def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        cv2.rectangle(img,button.pos,(x+w,y+h),(255,0,255,0.5),cv2.FILLED)
        cv2.putText(img,button.text,(x+25,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    # imgNew = np.zeros_like(img,np.uint8)
    # for button in buttonList:
    #     x,y=button.pos
    #     cvzone.cornerRect(imgNew,button.pos[1],button.pos[2],button.size[1],button.size[2],20,rt=0)
    #     cv2.rectangle(imgNew,button.pos,(x+button.size[1],y+button.size[2]),(255,0,255),cv2.FILLED)
    #     cv2.putText(imgNew,button.text,(x+40,y+60),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),3)
    # out = img.copy()
    # alpha = 0.5
    # mask=imgNew.astype(bool)
    # print(mask.shape)
    # out[mask]=cv2.addWeighted(img,alpha,imgNew,1-alpha,0)[mask]
    # return out
    return img

class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos=pos
        self.size=size
        self.text=text
    # def draw(self,img):
        
        # return img

buttonList = []
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([100*j+50,100*i+50],key))
# myButton = Button([100,100],"Q")
while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    img = detector.findHands(img)
    lmList,bboxInfo=detector.findPosition(img)
    img = drawAll(img,buttonList)
    # for list in lmList:
    #     list[2]-=40
    if lmList:
        # print(lmList)
        for button in buttonList:
            # print(button)
            x,y=button.pos
            w,h=button.size
            # print(x,y,w,h) 
            if x<lmList[8][1]<x+w and y<lmList[8][2]<y+h:
                cv2.rectangle(img,button.pos,(x+w,y+h),(200,0,200),cv2.FILLED)
                cv2.putText(img,button.text,(x+25,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                l,_,_=detector.findDistance(8,12,img, draw=False)
                # print(l)
                # when it is clicked
                if l < 60:
                    keyboard.press(button.text)
                    cv2.rectangle(img,button.pos,(x+w,y+h),(0,255,0),cv2.FILLED)
                    cv2.putText(img,button.text,(x+25,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                    finalText+=button.text 
                    sleep(0.5)

    cv2.rectangle(img,(50,350),(700,450),(175,0,175),cv2.FILLED)
    cv2.putText(img,finalText,(60,425),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    

    cv2.imshow("Image",img)
    cv2.waitKey(1)

