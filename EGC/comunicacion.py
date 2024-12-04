import time
import serial 
ser = serial.Serial('/dev/ttyACM0', baudrate=9600)
while True:
    data = ser.readline().decode('utf-8').rstrip()
    print(data)
    time.sleep(1)