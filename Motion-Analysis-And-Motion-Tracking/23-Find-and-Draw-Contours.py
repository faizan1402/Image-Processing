''' COntours can be joing the curve and explanation all the continous point along the boundry which
have the same color density
Contours tools can be used shape analysis  and object detection
 or object recognation
 By appliying can threshold and canny edge detection
Contours -Contours is a python list of all the contours in the image.each individual contour is a Numpy array of (x,y) coordinates of boundary of the object 


'''
import cv2 
img=cv2.imread('opencv-logo.png')# color image 
imgray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)# color img to grayscale img
ret ,thresh =cv2.threshold(imgray,127,255,0)
contours,hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours =" + str(len(contours)))	
print(contours[0])
cv2.drawContours(img,contours,-1,(0,255,0),3) #(img(original img),contour value (any value to ),(color),thickness )

cv2.imshow("Image",img)
cv2.imshow("Image Gray",imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Number of cotours =10
and img  seding
Cotours detection is a process can be simply as a curve joing all the continuous points(along with the boundry) having same colour or intensity .
the contours are a useful  tool for shape analysis and object detection and recognition.
'''