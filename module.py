import cv2 as cv
import mediapipe as mp
import pyautogui
import time

class handDetector():
    def __init__(self):
        self.mode = False
        self.max_num_hands = 2
        self.min_detection_confidence = 0.5
        self.min_tracking_confidence = 0.5

        self.drawing = mp.solutions.drawing_utils
        self.hands = mp.solutions.hands
        self.hand_obj = self.hands.Hands()
        self.tipIds = [4,8,12,16,20]

    def findHands(self, frm, draw=True):
        self.res = self.hand_obj.process(cv.cvtColor(frm, cv.COLOR_BGR2RGB))

        if self.res.multi_hand_landmarks:
            for hand_keyPoints in self.res.multi_hand_landmarks:
                if draw:
                    self.drawing.draw_landmarks(frm, hand_keyPoints, self.hands.HAND_CONNECTIONS)
        return frm

    def findPosition(self, frm, handNo=0):

        lmList = []
        if self.res.multi_hand_landmarks:
            myhand = self.res.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myhand.landmark):
                h,w,c =frm.shape
                cx,cy =int(lm.x*w),int(lm.y*h)

                lmList.append([id,cx,cy])

        return lmList


    
def main():

    cap = cv.VideoCapture(0)
    detector = handDetector()
    print(detector)
    while True:
        # end_time = time.time()
        success, frm = cap.read()
        frm = detector.findHands(frm)
        lmlist = detector.findPosition(frm)
        # if len(lmlist)!=0:
        #     print(lmlist[4])
        frm = cv.flip(frm, 1)
        cv.imshow("Image", frm)
        cv.waitKey(1)
        # cv.destroyAllWindows()
        # cap.release()
        # break
if __name__ == "__main__":
    main()