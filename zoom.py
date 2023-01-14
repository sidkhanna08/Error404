import cv2 as cv
from handTrackingmodule import handDetector

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

detector = handDetector()
initialDist = None
diff = 0
cx,cy = 250, 250

while True:
    success, frm = cap.read()
    hands, frm = detector.findHands(frm)
    frm1 = cv.imread("frm1.jpg")

    # frm = cv.flip(frm, 1)

    if len(hands) == 2:
        print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and\
                detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:

            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            if initialDist is None:
                length, info, frm = detector.findDistance((lmList1[8]),(lmList2[8]),frm)
                initialDist = length

            length, info, frm = detector.findDistance(lmList1[8], lmList2[8], frm)
            print(length)
            diff = int((length - initialDist)//2)
            cx,cy = info[4:]
    else:
        initialDist = None

    try:
        h1, w1, _=frm1.shape
        new_h,new_w = ((h1+diff)//2)*2, ((w1+diff)//2)*2
        frm1 =cv.resize(frm1,(new_w,new_h))
        frm[cy-new_h//2 : cy+new_h//2 , cx-new_w//2 : cx+new_w//2] = frm1
    except:
        pass


    cv.imshow("Image", frm)
    cv.waitKey(1)
