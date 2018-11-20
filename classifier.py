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

cv2.imwrite('mask.jpg', mask)
