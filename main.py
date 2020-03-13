from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
import serial
ser = serial.Serial('COM10', 9600)
while True:

    if "team" in str(GetWindowText(GetForegroundWindow)):
        ser.write("1")
    else:
        ser.write("0")