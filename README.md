# Teams Moniter
### Materials
- Arduino (I used a Micro)
- One LED
- One 220 ohm resistor (for the LED)
- One breadboard
- Two breadboard wires (I reccomend red and black)
### Software
- Arduino IDE
- Python 3 (and `pip`)
### Steps
*A  quick note: if you want to use a pre-built release, you will need to flash your Arduino, but skip the part after that. Instead, go to the Releases page (on GitHub) and download the latest release from there. Go to `/dist/main/` and run `main.exe` with the COM port of your Arduino as the argument after the filename (e.g. `main.exe COM10`*)  
Build this circuit:  
<img src="./Untitled Sketch_bb.svg">  
Once you have build the circuit, open the Arduino IDE, and flash the `SerialLEDMoniter.ino` sketch to the Arduino (remember to select the port!).  
In a CMD (or `bash`) shell, run `pip install pyinstaller`. Next, compile the Python script by going to the `Teams-Moniter` folder and running `pyinstaller main.py`. This will convert the script to an `exe` that you can run. Once it is done, go to `Teams-Moniter/dist/main/` and run `main.exe` with the COM port of the Arduino as the first argument (e.g. `main.exe COM10`).
