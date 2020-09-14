import numpy as np
import cv2 as cv
def nothing(x): # this is a call back function and changes the    
	print(x)# using call by function according color changes same window
#create a block image a window
img =np.zeros((300,512,3),np.uint8)#Black back ground is show 
#Same track baar in the same window 
cv.namedWindow('image')
cv.createTrackbar('B','image',0,255,nothing)#BGR  three track baar in same window
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)

switch='0 :OF\n 1: On'
cv.createTrackbar(switch,'image',0,1,nothing)

while (1) :
    cv.imshow('image',img)
    k=cv.waitKey(1) &0xFF

    if k==27:
	    break 
	b =cv.getTrackbarPos('B','image') #now this is three track baar channel  and check the same window

	g =cv.getTrackbarPos('G','image')
	r =cv.getTrackbarPos('R','image')
	s =cv.getTrackbarPos(switch,'image') # switch stament means the means set the channel '0' is the no color change and '1' is color  changes 
	# img[:] =[b,g,r]#image of the color track,so bgr channel is print the layout  
# We want to check the current track baar in img 
    if s==0:

     img[:] =0

     else :

   	   img[:] = [b,g,r]

cv.destroyAllWindows()