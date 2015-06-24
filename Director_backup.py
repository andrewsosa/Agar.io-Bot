import cv2
import cv2.cv as cv
import numpy as np

img = cv2.imread('pic1.png',0)
#cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.GaussianBlur(img,(5,5),0)



ret, img = cv2.threshold(img,210,255,cv2.THRESH_BINARY)

circles = cv2.HoughCircles(img, cv.CV_HOUGH_GRADIENT, 50, 1, param1=50, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
