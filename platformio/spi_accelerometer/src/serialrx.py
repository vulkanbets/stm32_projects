import time
import serial
from serial.serialutil import EIGHTBITS, PARITY_NONE, STOPBITS_ONE


ser = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=EIGHTBITS, stopbits=STOPBITS_ONE, parity=PARITY_NONE)


while(1):
    data = ser.readline().decode('ascii')
    print(data, end='')

