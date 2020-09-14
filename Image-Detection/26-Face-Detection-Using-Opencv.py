'''
First a classifier (namely a cascade of boosted classifiers working with haar -like features )
is trained with a few hundred sample views of a particular object (i.e a face or a car ),called positive examples ,that are scaled to the same size (say ,20*20),negative 
examples  -arbitrary images of the same size

'''

import cv2
face_cascade =cv2.CascadeClassifier('haarrcascade_frontalface_default.xml')#So this is harcascade file 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 



#Read the input image 
#img =cv2.imread('test.png')
cap =cv2.VideoCapture('Faizan-Face-Detection.mp4')

while cap.isOpened():


	_, cap = cap.read()# Basically applying thease frame

	gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces =face_cascade.detectMultiScale(gray,1.1,4)
	eyes =eye_cascade.detectMultiScale(roi_gray)

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
	for (x,y,w,h) in eyes:
		cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
  # Display the output 
	cv2.imshow('img',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

  	# All the four parameter draw the rectangle


  	  
  #objects =cv.CascadeClassifier.detectMultiScale(image,scaleFator,minNeighbors)
  #Image- Matrix of the type cv_8U containing an image where objects the detected object ,the rectangle may be partially outside the original image .
  #Scale Factor -Parameter specifying how much the image size is reduced at each image scale.

 # minNeighbors -Parameter specifying how many neighbors each candidate rectangle

  #should have to retain it .
  
   #faces =face_cascade.detectMultiScale(img,scalefactor,minNeighbors)

