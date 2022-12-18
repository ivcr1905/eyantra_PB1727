#QRDECODER USING pyzbar 

import cv2 as cv
import numpy as np
from pyzbar import pyzbar

img=cv.imread("G:\E-YATRA ROBOTICS COMPETITIONS\PB_Task1_Windows\PB_Task1_Windows\Task1B\public_test_cases\qr_1.png")
#gives the cordinates of the barcodes
barcodes=pyzbar.decode(img)
for barcode in barcodes:
	x,y,w,h=barcode.rect
	#cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
	a=int(x+w/2)
	b=int(y+h/2)
	#h=int(((a**2+b**2)**1/2)/2)
	cv.circle(img,(a,b),1,(0,0,255),5)
	bdata=barcode.data.decode("utf-8")
	btype=barcode.type



text= f"{bdata}"
cv.putText(img,text,(a+1,b+1),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
#cv.putText(img,text,(x,y),cv.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
cv.imshow("barcode",img)
cv.waitKey(0)


