import cv2
import cv2.cv as cv
import numpy as np

cap = cv2.VideoCapture(0)


# Read image
ret, frame = cap.read()

# Modify frame
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frame = cv2.medianBlur(frame,7)
ret,frame = cv2.threshold(frame,235,255,cv2.THRESH_TRUNC)


# Find Circles
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

# Display the resulting frame
cv2.imshow('frame',frame)

while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
