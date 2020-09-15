import cv2 
import matplotlib.pyplot as plt

cap =cv2.VideoCapture(0)

if cap.isOpened ():#When cap function through video is addopt
    ret,frame =cap.read()#cap function through video is read

    print(ret)
    print(frame)
else :
	ret =False
img1 =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

plt.imshow(img1)#matplotlib function through img is show 
  
plt.title(" Camera Image -1 ") #matplot lib
plt.xticks([])#xticks
plt.yticks([])

plt.show()
cap.release()#camera of port is release or camera adopter is release

