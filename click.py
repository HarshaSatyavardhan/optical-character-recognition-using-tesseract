import pytesseract
from gtts import gTTS
from PIL import Image 
import os
import cv2


cam = cv2.VideoCapture(0)
cv2.namedWindow('test')

while True:
    ret,frame = cam.read()                                                            
    cv2.imshow('test',frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("escape hit,closing...")
        break
    elif k%256 == 32:
        img_name = "frame.png".format()
        cv2.imwrite(img_name,frame)

cv2.waitKey(0)
cv2.destroyAllWindows()

