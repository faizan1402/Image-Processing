import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

img = cv.imread("lena.png")

#split the image BGR format
b,g,r = cv.split(img)
cv.imshow("img",img)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])


#200X200 means height and width

#img = np.zeros((200,200),np.uint8)

#cv.rectangle(img,(0,100),(200,200),(255),-1)#20,000 pixel of 255 
 # 15000 half of the pixel having 0 pixel of 127 added and 127 pixel of the height 5000
#cv.rectangle(img,(0,50),(100,100),(127),-1)

 # means np zeros means imge of black color pixel generate

#plt.hist(img.ravel(),256,[0,256])#hist function img,ravel,vertex,range 0 to 256

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()




''' Histograms is a graph and which is show of the area and plot the images
in area range and histograms showing the graph and intensity of pixel showing

'''