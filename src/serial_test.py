import serial
from random import randint

ser = serial.Serial('/dev/ttyACM0',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1)

while 1:
    x = ser.readline()
    print(x)