import cv2
import pytesseract
from pytesseract import * 
import re

img1 = cv2.imread('/home/rizzal/Documents/git/Python/OCR/eg1.jpeg')
text = pytesseract.image_to_string(img1)
print(text)

data = pytesseract.image_to_data(img1,output_type=Output.DICT)
# print(data)
print(data.keys())
print(data['conf'])
date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'
mail_pattern =	'^[a-z0-9](\.?[a-z0-9]){5,}@example\.net$'
n_box = len(data['text'])
print(n_box)
for i in range(n_box):
    if data['conf'][i]>50:
        if re.match(date_pattern,data['text'][i]) or re.match(mail_pattern,data['text'][i]) :
            x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
            cv2.rectangle(img1,(x,y),(x+w,y+h),color=(10,252,243),thickness=2)



cv2.imshow("Invoice",img1)
cv2.waitKey()
cv2.destroyAllWindows()