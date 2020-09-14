import cv2  
import numpy as np

def nothing(x) : #call back function  nothing
    print(x)
     #crete a black image window

img =np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')# create window name loaded

cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

# How to used switch variable
switch ='0: OFF\n 1:ON' # if switch value is off then no color is changes and switch is on then color is changes
cv2.createTrackbar(switch,'image',0,1,nothing)

while(1):
	cv2.imshow('image',img)
	k =cv2.waitKey(1) & 0xFF

	if k == 27 : # this means indent always one is give tab key se dena h
	   break

   # color is changes  


	b =cv2.getTrackbarPos('B','image')
	g =cv2.getTrackbarPos('G','image')
	r =cv2.getTrackbarPos('R','image')
	s =cv2.getTrackbarPos(switch,'image')# switch function is the color is changes

	if s ==0:

		img[:] =0
	else :

	    img[:] =[b,g,r]


cv2.destroyAllWindows() 
