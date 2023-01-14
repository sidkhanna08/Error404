import cv2
from handTrackingmodule1 import handDetector

cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)

detector2 = handDetector()
initialDist = None
diff = 0
cx1,cy1 = 250, 250

while True:
    success, frm = cap.read()
    hands, frm = detector2.findHands(frm)
    # frm = cv2.imread("frm.jpg")

    # frm = cv2.flip(frm, 1)
    # frm=cv2.flip(frm,1)
    if len(hands) == 2:
        # print(detector2.fingersUp(hands[0]),detector2.fingersUp(hands[1]))
        if detector2.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and\
                detector2.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:

            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if initialDist is None:
                length, info, frm = detector2.findDistance((lmList1[8]),(lmList2[8]),frm)
                initialDist = length

            length, info, frm = detector2.findDistance(lmList1[8], lmList2[8], frm)
            # print(length)
            diff = int((length - initialDist)//2)
            cx1,cy1 = info[4:]
    else:
        initialDist = None

    try:
        h1, w1, _=frm.shape
        new_h,new_w = ((h1+diff)//2)*2, ((w1+diff)//2)*2
        frm =cv2.resize(frm,(new_w,new_h))
        frm[cy1-new_h//2 : cy1+new_h//2 , cx1-new_w//2 : cx1+new_w//2] = frm
    except:
        pass


    cv2.imshow("Image", frm)
    cv2.waitKey(1)
