from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
import serial
from sys import argv, exit
try:
    ser = serial.Serial(argv[1], 9600)
except IndexError:
    print("Include the desired COM port as the first argument")
    exit(7)
while True:
    if "Teams" in str(GetWindowText(GetForegroundWindow())):
        ser.write(b"1")
    else:
        ser.write(b"0")