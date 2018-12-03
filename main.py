import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import classifier
import range

GPIO.setmode(GPIO.BCM)

trig_pin = 23
echo_pin = 24
led_pin = 16

try:
	GPIO.setup(led_pin,GPIO.OUT)
	GPIO.output(led_pin, GPIO.HIGH)

	range_sensor = range.RangeSensor(trig_pin, echo_pin)

	# Initialize distance sensor

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

		# Verify range to target (one ping only)
		range = range_sensor.get_reading()

		if rect is None:
			# Don't see no red
			print("No red, man        ", end="\r")
			pass
		else:
			vector = (rect[0] + (rect[2] / 2) - 320) / 320
			print("frame", frame_number, "vector", vector, "range", range, end="\r")

		# Determine the new vector
		# Determine the new speed
		# Set course for adventure

		# Clear out for next frame
		rawCapture.truncate(0)

		# Next frame
		frame_number = frame_number + 1
finally:
	GPIO.cleanup()
