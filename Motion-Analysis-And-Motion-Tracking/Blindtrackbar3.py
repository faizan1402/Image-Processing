''' I' m using two trackbar and two track scale color to gray scale


'''

     
import cv2
import numpy as np
def nothing(x) :
	print(x)
cv2.namedWindow('image')
cv2.createTrackbar('CP','image',10,400,nothing)# means CP is current position and text start 10 to 400 maximum
switch ='color/gray' #means color image to gray image convert
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1) :
	img =cv2.imread('lena.png')
	img =cv2.imshow('image',img)
	pos =cv2.getTrackbarPos('CP','image')# CP menas current trackbar
	font =cv2.FONT_HERSHEY_SIMPLEX # Means different types of font size

	cv2.putText(img,str(pos),(50,150),font,4,(0,0,255))# write the text inside image

	k =cv2.waitKey(1) & 0xFF 
	if k==27:
		break 
	s =cv2.getTrackbarPos(switch,'image')

	if s ==0:
		pass #means switch of value is '0' then no changes the color
	else :

		img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		img =cv2.imshow('image',img)

cv2.detroyAllWindows()


