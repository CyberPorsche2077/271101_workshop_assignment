#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Name="Porsche"
Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cx8 = cx
                if id == 7:
                    id7 = int(id)
                    cx7 = cx
                if id == 12:
                    id12 = int(id)
                    cx12 = cx
                if id == 11:
                    id11 = int(id)
                    cx11 = cx
                if id == 16:
                    id16 = int(id)
                    cx16 = cx
                if id == 15:
                    id15 = int(id)
                    cx15 = cx
                if id == 20:
                    id20 = int(id)
                    cx20 = cx
                if id == 19:
                    id19 = int(id)
                    cx19 = cx
            Tfing="Thumb"
            Ifing="Index_Finger"
            Mfing="Middel_Finger"
            Rfing="Ring_Finger"
            Pfing="Pinky"
            if cx3 < cx4:
                cv2.putText(img, str(str(Tfing)), (250, 150), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
            if cx7 < cx8:
                cv2.putText(img, str(str(Ifing)), (250, 200), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
            if cx11 < cx12:
                cv2.putText(img, str(str(Mfing)), (250, 250), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
            if cx15 < cx16:
                cv2.putText(img, str(str(Rfing)), (250, 300), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
            if cx19 < cx20:
                cv2.putText(img, str(str(Pfing)), (250, 350), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
            else:
                Nfing = 5

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.putText(img, str(str(Name)), (425, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 165, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()