import cv2 
import numpy as np

#So video capture the videocapture function is used  video detect the video

cap =cv2.VideoCapture("Motion-detection.mp4")

ret, frame1 =cap.read()

ret, frame2 =cap.read()


while cap.isOpened() :# isOpened 
    
	diff =cv2.absdiff(frame1,frame2) # diff basically

	gray =cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY) #Convert the color image to gray image

	blur =cv2.GaussianBlur(gray ,(5,5),0)# Gaussian function basically blur the image

	_,thresh=cv2.threshold(blur ,20,255,cv2.THRESH_BINARY)

	dilated =cv2.dilate(thresh,None,iterations=3)

	contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for contour in contours : #means countour is seperate and reactangle print
		(x,y,w,h) =cv2.boundingRect(contour)

		if cv2.contourArea(contour)<700 : #If the area contour greater than then rectangle is print 
		   continue
		cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2) #(x,y)direction and color ,thickness

		# inside image put text frame(frame1,status,format,movement (X,y direction),(design  of font),font scale ,font color,thickness)

		cv2.putText(frame1,"status :()".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)


	    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)# (frame1 draw contours,(no of color),no of thickness)

	#contour detect the image corner part

	cv2.imshow("Motion-detection and tracking object",frame1)
	frame1=frame2


	ret , frame2 =cap.read() # reading the new frame1 and frame2

	if cv2.waitKey(40)==27:

		brea

cv2 .destroyAllWindows()

cap.release()

   
   
       #so this code only detect the motion but not detect the reactangle size and shape and not remove the 
       # noise and traffic noise . 

        #Imppoint -1  So this part code only basically remove the noise on road and also roap  remove the noise and draw the rectangle 

       # for contour in contours : #means countour is seperate and reactangle print
		#(x,y,w,h) =cv2.boundingRect(contour)

		#if cv2.contourArea(contour)<700 : #If the area contour greater than then rectangle is print 
		  # continue
		#cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2) #(x,y)direction and color ,thickness

		#inside image put text frame(frame1,status,format,movement (X,y direction),(design  of font),font scale ,font color,thickness)

		#cv2.putText(frame1,"status :()".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
		


		


 