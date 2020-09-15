''' Edge detection is basically gray  scale img form
1 - Original img is convert the gray scale img and blur operation is used 

'''
import cv2  

def sketch(image) :# Creating sketch function 


# img convert the grayscale img  

	img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Convert the gray scale

	img_gray_blur =cv2.GaussianBlur(img_gray,(5,5),0) # GausianBlur function (img_gray(kernel 5x5),0) 
#Edge detection basically  using Canny function cv2.Canny

	canny_edge = cv2.Canny( img_gray_blur,10,70) #Canny function basically very smoothly img is blur and pixel is detect and lower threshold(10) and upper threshold(70)
# So img we are see the binary img form and return the mask value
#ret ,mask =cv2.threshold(canny_edge,threshold value(70),maximum value 255,cv2.THRESH_BINARY)

	ret ,mask =cv2.threshold(canny_edge,70,255,cv2.THRESH_BINARY) # Or THRESHINVERSE used 



	return mask

cap = cv2.VideoCapture(0) #This function basically for video capture

while True :
    
    ret ,frame = cap.read() #read the frame

    cv2.imshow("Our Live Sktech",sketch(frame)) #Basically sktech through ,image detect out put provide 

    if cv2.waitKey(1) == 13:  # 13 statement break the stament
    	break 

cap.release()
cv2.destroyAllWindows()



