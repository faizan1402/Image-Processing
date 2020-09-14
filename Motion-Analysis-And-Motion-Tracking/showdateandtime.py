import cv2
cap =cv2.videoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3,3000)
cap.set(4,3000)
print(cap.get(3))
print(cap.get(4))

while(cap.isOpned()):
	rat,frame =cap.read()
	if ret ==True:
		gray =cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)

		if cv2.waitKey(1) oxFF==ord('q'):
			break
		else :
			break
cap.release()
cv2.destroyAllWindows()