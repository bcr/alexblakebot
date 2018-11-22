from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import classifier


# Initialize distance sensor

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	raw_frame = frame.array

	# Identify the target rectangle
	rect = classifier.target_rect_from_frame(raw_frame)

	if rect is None:
		# Don't see no red
		print("No red, man        ", end="\r")
		pass
	else:
		vector = (((rect[0] + rect[2]) / 2) - 320) / 320
		print("Vector", vector, end="\r")

	# Clear out for next frame

	rawCapture.truncate(0)

# Determine the new vector
# Determine the new speed
# Set course for adventure
