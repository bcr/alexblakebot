from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
with PiCamera() as camera:
	rawCapture = PiRGBArray(camera)

	# allow the camera to warmup
	time.sleep(0.1)

	# grab an image from the camera
	camera.capture(rawCapture, format="rgb")
	frame = rawCapture.array

	# Save the resulting image
	cv2.imwrite('bar.jpg', frame)
