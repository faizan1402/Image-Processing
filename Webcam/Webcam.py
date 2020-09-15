''' How to start webcam 
Webcam is not image only loop infinite run 
And how to  live online 

'''
import cv2
#Videocapture function through video capture
cap =cv2.VideoCapture(0)#cap variable through video is capture

while True :# infinite loop 
 	ret,frame =cap.read( ) #ret (return value) variable through value is hold and cap read the value

 	cv2.imshow('Our Live sketch',frame)

 	if cv2.waitKey(1)==13:

 		break #Means break is stop the camera value 
cv2.release() #release basically camera port release the all the port

cv2.destroyAllWindows()