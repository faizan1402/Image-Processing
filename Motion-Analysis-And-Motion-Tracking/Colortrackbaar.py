import cv2  
import numpy as np

def nothing(x):
	pass

img = np.zeros((300,512,3),np.uint8)

cv2.namedWindow("image")

cv2.createTrackbar("R",image,0,255,nothing)
cv2.createTrackbar("G",image,0,255,nothing)
cv2.createTrackbar("B",image,255,nothing)

switch ='0 :OFF \n 1 : ON'#when switch is 0 then off work and switch is on then

cv2.createTrackbar(switch,'image',0,1,nothing)  #starting value is '0' and maximum is '1'

while True :
	 cv2.imshow('image',img)

	 if cv2.waitKey(1) == 13 :
		 break 
		#image trackbar of position find

	 r =cv2.getTrackbarPos('R','image')

	 g =cv2.getTrackbarPos('G','image')
	 b =cv2.getTrackbarPos('B','image')
	 s =cv2.getTrackbarPos(switch,'image')

     if s== 0:
    	 img[:] = 0
     else :
    	 img[:] =[b,g,r]

cv2.destroyAllWindows(0)




