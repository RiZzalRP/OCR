# from image text extract and character read or recoganization

# library used is pytesseract 

import cv2
import pytesseract
from pytesseract import *

img1= cv2.imread('/home/rizzal/Documents/git/Python/OCR/7.png')
text = pytesseract.image_to_string(img1)   # to extract the string  in the image and 
# print(text)                                 # print the string
data =pytesseract.image_to_data(img1,output_type=Output.DICT)
print(data.keys())
print(data['text'])
print(data['conf'])

# Drw rectangle on text

n_box = len(data['text'])  # no of box to draw and its count
print(n_box)

for i in range(n_box):
    if data['conf'][i]>80:
        x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
        cv2.rectangle(
        img1,
        (x,y),
        (x+w,y+h),
        color=(0,255,5),
        thickness=2
      )


cv2.imshow("",img1)
cv2.waitKey()
cv2.destroyAllWindows()