import cv2
import numpy as np
#When you re not read the image only black back ground 
#Only text and shape show using 
img =np.zeros([512,512,3],np.uint8)

#img =cv2.imread('lena.png',1)
# show the line img (x of co - ordinate),(y of co-ordinate),(BGR color channel value show),(255(Blue),0,0),(0,(Green),0),(0,0,(Red)),(Number thickness of line)
img =cv2.line(img,(0,0),(255,255),(147,96,44),12)
# 146,96,44(BGR oreder)
img =cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),15)
# arrowedLine function image og the co - ordinate value means channel value change
#How to add rectangle inside the image 
#So  using top (left co-ordinate) and (bottom right co-ordinate) ,number thickness)
img =cv2.rectangle(img,(384,0),(510,128),(255,0,0),10)
# How to add the circle in the image
#circle(img ,center,radius),n of thickness x and y )
img =cv2.circle(img,(447,63),63,(0,255,0),-1)
font =cv2.FONT_HERSHEY_SIMPLEX
img =cv2.putText(img,'Opencv',(10,500),font,4,(0,255,0), 10 , cv2.LINE_AA)




cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()