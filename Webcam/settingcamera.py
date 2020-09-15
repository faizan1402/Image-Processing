import cv2
import datetime 

cap =cv2.VideoCapture(0)
print(cap.get(cv2.CAP_FRAME_WIDTH))
print(cap.get(cv2.CAP_FRAME_HEIGHT))

#cap.set(3,3000)
#cap.set(4,3000)
#print(cap.set(3))
#print(cap.set(4))
while(cap.isopened()):
	ret,frame =cap.read()
	if ret==True :
		font =cv2.FONT_HERSHEY_SIMPLEX
		text ='Width :'+st.datetr(cap.get(3)) +'Height :' +str(cap.get(4))
		datet =str(datetime.datetimenow())
		frame =cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & oxFF==ord('q'):
			break 
		else :
			break
cap.release()
cv2.destroyAllWindows()
