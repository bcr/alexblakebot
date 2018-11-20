import serial

baudrate=38400

ser = serial.Serial(port='/dev/ttyS0', baudrate = baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
while True:
	speed = input("Enter speed: ")
	intspeed = int(speed)
	print("Setting speed", intspeed)
	ser.write(chr(intspeed).encode('iso-8859-1'))
