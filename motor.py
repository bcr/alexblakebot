import serial

baudrate=38400

class MotorController:
	def __init__(self):
		self.ser = serial.Serial(port='/dev/ttyS0', baudrate = baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

	def set_speed(self, left, right):
		# Input left and right are values from -1.0 to 1.0 where -1.0 is full reverse, 1.0 is full forward, and 0 is stop

		# Motor 1 speed is 1-127   where 64  is "stop" and 1   is "full reverse" and 127 is "full forward"
		# Motor 2 speed is 128-255 where 192 is "stop" and 128 is "full reverse" and 255 is "full forward"
		# Speed 0 is "all stop"

		left_speed  = 64  + (left * 63)
		right_speed = 192 + (right * 63) # This will actually generate values from 129-255. Shh.

		self.send_byte(left_speed)
		self.send_byte(right_speed)

	def stop(self):
		self.send_byte(0)

	def send_byte(self, value):
		self.ser.write(bytes([int(value)]))
