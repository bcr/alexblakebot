from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

import classifier

try:
	camera = PiCamera()
	camera.resolution = (640, 480)
	camera.framerate = 32
	rawCapture = PiRGBArray(camera, size=(640, 480))

	# allow the camera to warmup
	time.sleep(0.1)

	frame_number = 1

	for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
		raw_frame = frame.array

		# Identify the target rectangle
		rect = classifier.target_rect_from_frame(raw_frame)

		# Write out the frame

		[x,y,w,h] = rect
		cv2.rectangle(raw_frame,(x,y),(x+w,y+h),(0,255,0),5)

		cv2.imwrite('classified.jpg', raw_frame)

		# Clear out for next frame
		rawCapture.truncate(0)

		# Next frame
		frame_number = frame_number + 1
		break
finally:
	pass

print("Exited.")
