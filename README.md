# Teams Monitor
> ⚠️IMPORTANT: This repository moved to the [Cinematic Meeting Sign](https://github.com/CoconutMacaroon/Cinematic-Meeting-Sign) repo instead. This repo will continue to be avaliable, but changes should be in the other repo. Also, these directions will not be udpated. I made [an Instructable](https://www.instructables.com/id/Cinematic-Sign-for-Video-Conferencing/) that is (roughly) based on these directions, but uses a Cinematic Lightbox rather than an LED, which has more up-to-date (and specific) directions.
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
Run the command `pip install pyserial`. That will install the library that Python uses to talk to your Arduino.  
*A  quick note: if you want to use a pre-built release, you will need to flash your Arduino, but skip the part after that. Instead, go to the Releases page (on GitHub) and download the latest release from there. Go to `/dist/main/` and run `main.exe` with the COM port of your Arduino as the argument after the filename (e.g. `main.exe COM10`*)  
Build this circuit:  
<img src="./Untitled Sketch_bb.svg">  
Once you have build the circuit, open the Arduino IDE, and flash the `SerialLEDMoniter.ino` sketch to the Arduino (remember to select the port!).  
In a CMD (or `bash`) shell, run `pip install pyinstaller`. Next, compile the Python script by going to the `Teams-Moniter` folder and running `pyinstaller main.py`. This will convert the script to an `exe` that you can run. Once it is done, go to `Teams-Moniter/dist/main/` and run `main.exe` with the COM port of the Arduino as the first argument (e.g. `main.exe COM10`).
### Helping Out
> ⚠️IMPORTANT: This repo is being archived. Please do not submit PR's to this repo.<br><br>
If something isn't working right, create an issue. Also, if you get an error, please report it as an issue, because other people will probobly also be getting said error. Once the problem has been resovled, create a seperate branch containing the fix. Once you have done that, create a PR (pull request) to merge the two branches.
