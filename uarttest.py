import time
import serial

baudrate=38400

ser = serial.Serial(port='/dev/ttyS0', baudrate = baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)
counter=0
while 1:
               print("Writing counter", counter)
               ser.write(chr(counter).encode("utf-8"))
#               ser.write('Write counter: %d \n'%(counter))
               time.sleep(1)
               counter += 1
