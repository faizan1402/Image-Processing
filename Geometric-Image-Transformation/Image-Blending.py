import cv2 
import numpy as np
apple =cv2.imread('apple.jpg')
orange=cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
apple_orange = np.hstack((apple[:,:256],orange[:,256:]))
cv2.imshow("apple",apple)
cv2.imshow("orange",orange)
cv2.imshow("apple_orange",apple_orange)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
Means adding two half images because canctination image means add two img
(apple +orange =blending img)