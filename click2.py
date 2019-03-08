import cv2
from gtts import gTTS
from PIL import Image
import os
import pytesseract





image = cv2.imread('frame.png')
gray = cv2.cvtColor(image,0)


cv2.imwrite('gray.jpg',gray)
img = Image.open('gray.jpg')
result  = pytesseract.image_to_string(img)
print(result)



tts = gTTS(text = result , lang = 'en')
path = '/home/pi/sound.mp3'
tts.save("sound.mp3")






