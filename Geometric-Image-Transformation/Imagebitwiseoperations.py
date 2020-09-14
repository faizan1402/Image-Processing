#Bitwise Operation
import cv2
import numpy as np


square =np.zeros((300,300),np.uint8)
#np.zeros(img of value),np.uint8(data type unsigned data type used)
cv2.rectangle(square,(50,50),(250,250),255,-1)
#cv2.rectangle function( inside square (starting value),(ending value,(white color ) ,thickness of shape (bt -1 coloe is field whole square))
#when starting value increase then square is small shape and ending value increase then square is changes and different position will shift
#But normal square is show starting value is (height,weidth)(50,50) and ending vslue is (250,250) size is requirement 

#Making as eclipse

cv2.imshow("Square",square)
cv2.waitKey(0)

ellipse =np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("Ellipse",ellipse)
cv2.waitKey(0)
 
 #bitwise and operator used 
And =cv2.bitwise_and(square,ellipse)#comparasion square and ellipse 
cv2.imshow("AND",And)
#Means merge  the shape square and ellipse both are merge
cv2.waitKey(0)

#bitwise or operator
#OR operator is the add the shape and output is '1' is hide and input is 0 and 1 then out put is '1' will come

Or =cv2.bitwise_or(square,ellipse)
cv2.imshow("OR",Or)
cv2.waitKey(0)

#bitwise x-or operator
Xor =cv2.bitwise_xor(square,ellipse)
cv2.imshow("XOR",Xor)
cv2.waitKey(0)

#bitwise Not operator 

Not =cv2.bitwise_not(square,ellipse)
cv2.imshow("NOT",Not)

cv2.waitKey(0)

cv2.destroyAllWindows()


#Binary img is '0' and '1' and zero is black color and one is white color
