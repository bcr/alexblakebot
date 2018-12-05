import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import classifier
import range
import motor

GPIO.setmode(GPIO.BCM)

trig_pin = 23
echo_pin = 24
led_pin = 16
minimum_feature_size = 500

motor = motor.MotorController()

def clamp(n, minn, maxn):
	return max(min(maxn, n), minn)

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

		if (rect is None) or ((rect[2] * rect[3]) < minimum_feature_size):
			# Don't see no red
			vector = None
		else:
			# Determine the new vector
			vector = (rect[0] + (rect[2] / 2) - 320) / 320

		print("frame", frame_number, "vector", vector, "range", range, "rect", rect)

		# Determine the new speed
		# As we get closer, slow down. So when we get to 25cm be stopped, slowing down over 100cm
		speed = (range - 25) / 100
		speed = clamp(speed, 0.0, 1.0)

		if vector is not None:
			# Figure out the motor inputs based on speed and vector
			absvector = abs(vector)
			speed_1 = absvector * speed
			speed_2 = (1.0 - absvector) * speed

			if (vector < 0):
				left_motor_speed = speed_1
				right_motor_speed = speed_2
			else:
				right_motor_speed = speed_1
				left_motor_speed = speed_2

		else:
			# Spin in a circle until you find something
			left_motor_speed = 0.5
			right_motor_speed = -0.5

		# Set course for adventure
		print("left_motor_speed", left_motor_speed, "right_motor_speed", right_motor_speed)
		motor.set_speed(left_motor_speed, right_motor_speed)

		# Clear out for next frame
		rawCapture.truncate(0)

		# Next frame
		frame_number = frame_number + 1
finally:
	motor.stop()
	GPIO.cleanup()
