import cv2
from matplotlib import pyplot as plt

img =cv2.imread("lena.png",-1)
cv2.imshow("Image",img)
#img =cv2.cvtColor( img,cv2.COLOR_BGR2RGB)#Means orginal to RGB format 

plt.imshow(img)# using matplotlib (RBG format  )
plt.xticks([]),plt.yticks([])#Image the pixel x and y axis

plt.show() #this is the show the matplot lib

cv2.waitKey(0)

cv2.destroyAllWindows()
