from win32gui import GetWindowText, GetForegroundWindow
from time import sleep
print(GetWindowText(GetForegroundWindow()))
while True:
    focused_window = GetWindowText(GetForegroundWindow)
    