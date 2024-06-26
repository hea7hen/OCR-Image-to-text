import pytesseract
import PIL.Image
import cv2
from pytesseract import Output
"""
Page segmentation modes:

    0   Orientation and script detection (0SD) only.
    1   Automatic page segmentation with OSD.
    2   Automatic page segmentation, but no OSD, or OCR.
    3   Fully automatic page segmentation, but no OSD. (Default)
    4   Assume a single column of text of variable sizes.
    5   Assume a single uniform block of vertically aligned text.
    6   Assume a single uniform block of text.
    7   Treat the image as a Single text Line.
    8   Treat the image as a single word.
    9   Treat the image as a single word in a circle.
   10   reat the image as a single character.
   11   Sparse text. Find as much text as possible in no particular order.
   12   sparse text with OSD.
   13   Raw Line. Treat the image as a single, text Line, bypassing hacks that are Tesseract-speci
"""

"""
OCR Engine Mode
0    Legacy engine only.

1    Neural nets LSTM engine only.

2    Legacy + LSTM engines.

3   Default, based on what is available.
"""

myconfig = r"--psm 6 --oem 3" #For a basic plain text image with clear texts
logoconfig = r"--psm 11 --oem 3" # For logos

text = pytesseract.image_to_string(PIL.Image.open("logo.jpg"),config=logoconfig)

img = cv2.imread("logo.jpg")
height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

# print(text) #Prints every output
print(data["text"]) #prints recogonised texts

amount_boxes = len(data['text'])

for i in range(amount_boxes):
    if float(data['conf'][i] > 80):
        (x,y,width,height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)

cv2.imshow("img",img)
cv2.waitKey(0)