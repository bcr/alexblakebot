import RPi.GPIO as GPIO
import time

class RangeSensor:
	def __init__(self, trig_pin, echo_pin):
		self.trig_pin = trig_pin
		self.echo_pin = echo_pin
		GPIO.setup(self.trig_pin,GPIO.OUT)
		GPIO.setup(self.echo_pin,GPIO.IN)
		GPIO.output(self.trig_pin, False)

	def get_reading(self):
		GPIO.output(self.trig_pin, True)
		time.sleep(0.00001)
		GPIO.output(self.trig_pin, False)

		while GPIO.input(self.echo_pin)==0:
			pulse_start = time.time()

		while GPIO.input(self.echo_pin)==1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration * 17150

		distance = round(distance, 2)

		return distance
