import cv2
import numpy as np

def target_rect_from_frame(frame):
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

	return rects[0] if (len(rects) >= 1) else None
