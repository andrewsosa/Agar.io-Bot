import cv2
import cv2.cv as cv
import numpy as np

path = "images/"
file = "light1.png"

# Read image
frame = cv2.imread(path+file)

# Modify frame
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.medianBlur(frame,7)

# Find circles
circles = cv2.HoughCircles(frame, cv.CV_HOUGH_GRADIENT, 1, 30,
                            param1=50, param2=30, minRadius=0, maxRadius=0)

# Graph circles
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
    #print i

# Show circles
cv2.imshow('detected circles',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
