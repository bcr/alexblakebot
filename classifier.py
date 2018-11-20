import cv2
import numpy as np

# Set up image as required
input_filename = "bar.jpg"

frame = cv2.imread(input_filename)

# Do image stuff
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([110,50,50])
upper_red = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)

# mask should now have 1 bits where there is red

# Find the contours
im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

rects = map(lambda contour: cv2.boundingRect(contour), contours)

rects = sorted(rects, reverse=True, key=lambda rectangle1: (rectangle1[2] * rectangle1[3]))

rect = rects[0]

[x,y,w,h] = rect
cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

cv2.imwrite('mask.jpg', frame)
