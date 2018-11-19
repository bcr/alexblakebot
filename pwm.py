import RPi.GPIO as GPIO
import time

PWM = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM, GPIO.OUT)

try:
	p = GPIO.PWM(PWM, 500)

	p.start(25)
	try:
		input('Press return to stop:')
	finally:
		p.stop()
finally:
	GPIO.cleanup()
