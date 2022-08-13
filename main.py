from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import mediapipe as mp

def start():
    global cap,frame
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    video()

def video():
    global cap,frame
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=640)
            frame = cv2.flip(frame, 1)
            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            mpHands = mp.solutions.hands
            hands = mpHands.Hands()
            mpDraw = mp.solutions.drawing_utils

            result = hands.process(frame)
            # print(result.multi_hand_landmarks)
            if result.multi_hand_landmarks:
                for handLms in result.multi_hand_landmarks:
                    mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
                    if (handLms.landmark[mpHands.HandLandmark.PINKY_DIP].y > handLms.landmark[mpHands.HandLandmark.PINKY_TIP].y and
                            handLms.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y > handLms.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y > handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y > handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y and
                            handLms.landmark[mpHands.HandLandmark.THUMB_IP].x > handLms.landmark[mpHands.HandLandmark.THUMB_TIP].x):
                        lab = Label(root, text="Gesture : Peace")
                        lab.grid(column=0, row=2, padx=5, pady=5)
                        lab.configure(font=("Times New Roman", 20, "bold"))


                    elif (handLms.landmark[mpHands.HandLandmark.PINKY_TIP].y < handLms.landmark[mpHands.HandLandmark.PINKY_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y < handLms.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y < handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y < handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.THUMB_TIP].x < handLms.landmark[mpHands.HandLandmark.THUMB_IP].x):
                        lab = Label(root, text=" Gesture : HI  ")
                        lab.grid(column=0, row=2, padx=5, pady=5)
                        lab.configure(font=("Times New Roman", 20, "bold"))

                    elif (handLms.landmark[mpHands.HandLandmark.PINKY_TIP].y > handLms.landmark[mpHands.HandLandmark.PINKY_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.RING_FINGER_TIP].y > handLms.landmark[mpHands.HandLandmark.RING_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_TIP].y > handLms.landmark[mpHands.HandLandmark.MIDDLE_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP].y > handLms.landmark[mpHands.HandLandmark.INDEX_FINGER_DIP].y and
                            handLms.landmark[mpHands.HandLandmark.THUMB_TIP].x < handLms.landmark[mpHands.HandLandmark.THUMB_IP].x):
                        lab = Label(root, text="Gesture : Okay")
                        lab.grid(column=0, row=2, padx=5, pady=5)
                        lab.configure(font=("Times New Roman", 20, "bold"))
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, video)
        else:
            lblVideo.image = ""
            cap.release()

def end():
    global cap
    cap.release()

cap = None
root = Tk()

btnIniciar = Button(root, text="start", width=45, command=start)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)

btnFinalizar = Button(root, text="end", width=45, command=end)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)

root.mainloop()