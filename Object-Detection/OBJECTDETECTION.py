import cv2
import numpy as np

def nothing(x) :
	pass 
 
while True :
	 frame =cv2.imread ("circlesdetect.png") 

	 hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

	  #HSV of the blue color image detect 

	 l_b =np.array([110,50,50]) # lower boundation  of blue color detect the image 
	 u_b =np.array([130,255,255]) #upper boundation of blue color

	 mask =cv2.inRange(hsv,l_b,u_b )

	 res =cv2.bitwise_and(frame,frame,mask=mask)

	 cv2.imshow("frme",frame,) #mask function only detect the object 
	 cv2.imshow("mask",mask)
	 cv2.imshow("res",res)


#cv2.imshow("frame",frame)

	 key =cv2.waitKey(1) 

	 if key ==27 :
	 	break

cv2.destroyAllWindows()