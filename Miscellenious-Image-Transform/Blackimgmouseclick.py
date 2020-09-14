import cv2
import numpy as np

def click_event(event,x,y,flags,param) :#click function

	if event ==cv2.EVENT_LBUTTONDOWN :
		cv2.circle(img,(x,y),3,(0,255,0),-1)# center of circle and radius
		points.append((x,y))
		if len(points) >=2 :#if points between two points
			cv2.line(img,points[-1],points[-2],(255,0,0),5)#(img,points[last index],point[Last to last index])
		cv2.imshow("Image",img)
img=np.zeros((512,512,3),np.uint8)#back ground iS back form
cv2.imshow("Image",img)#show the out put image
points=[]
cv2.setMouseCallback('Image',click_event)# Mouse function call
cv2.waitKey(0)
cv2.destroyAllWindows()

