import cv2
import mediapipe as mp
import time
import webbrowser
import HandTrackingModule as htm


pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img1 = cap.read()
    img1 = detector.findHands(img1, draw=True)
    lmList = detector.findPosition(img1, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

        if lmList[4]:
            webbrowser.open("www.google.com")
            break
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    #cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
     #           (255, 0, 255), 3)

    cv2.imshow("Image", img1)
    cv2.waitKey(1)