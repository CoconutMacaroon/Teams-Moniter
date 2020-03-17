import serial
from sys import argv, exit

try:
    ser = serial.Serial(argv[1], 9600)
    ser.write('t'.encode())
    if (str(ser.read(size=7)) == "UNITTEST"):
        print("[OK] Serial")
    else:
        print("[FAILED] Serial")
except IndexError:
    print("Include the desired COM port as the first argument")
    exit(7)

import importlib
spam_loader = importlib.find_loader('serial')
found = spam_loader is not None

if(found == True):
    print("[OK] Serial installed")
else:
    print("[FAILED] Serial installed")
