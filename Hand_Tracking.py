import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

PreviousTime = 0
CurrentTime = 0


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for HandLandmarks in results.multi_hand_landmarks:
            for ID, Landmark in enumerate(HandLandmarks.landmark):
                #print(ID,Landmark)
                height, width, channel =img.shape
                Centerx, Centery = int(Landmark.x*width) ,int(Landmark.y*height)
                print(ID, Centerx, Centery)
                if ID==0:
                    cv2.circle(img, (Centerx,Centery), 20, (0,255,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, HandLandmarks, mpHands.HAND_CONNECTIONS)

    CurrentTime = time.time()
    fps = 1/(CurrentTime-PreviousTime)
    PreviousTime = CurrentTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,0), 3)



    cv2.imshow("Image", img)
    cv2.waitKey(1)


