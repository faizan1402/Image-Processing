import cv2
import numpy as np
#events ={i for i in dir(cv2) if 'EVENT'in i }
#print(events)

def click_event(event,x,y,flag ,param) :
   if event ==cv2.EVENT_LBUTTONDOWN : #leftbutton

     print(x,',',y)

     font =cv2.FONT_HERSHEY_SIMPLEX #Basically find the font size
     strXY =str(x) + ' ,' +str(y)# + is cancatination

     cv2.putText(img,strXY,(x,y),font,.6,(255,255,0),2)
     cv2.imshow('image',img)

   if event == cv2.EVENT_RBUTTONDOWN :#Rightbutton

     Blue  = img[y,x,0] # index '0' channel (blue color)
     Green = img[y,x,1] #index '1' channel (Green color)
     Red   = img[y,x,2] #index '2' channel (Red color)

     font =cv2.FONT_HERSHEY_SIMPLEX #Basically find the font size
     strBGR =str(Blue) + ' ,' +str(Green) + ',' + str(Red) # + is cancatination

     cv2.putText(img, strBGR , (x ,y) , font , .6 ,(0,255,255),2)
     cv2.imshow('image',img)

img =cv2.imread('lena.png')
cv2.imshow("image",img)
#img =np.zeros((512,512,3),np.uint8)
# np.zeros basically using black background and uint8 (datatype)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()