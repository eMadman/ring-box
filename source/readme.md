# Usage Instructions
* Place camera.py in /home/pi
* Run script from shell with ./camera.py to verify functionality
* If using PiSugar 3 module, [install necessary software](https://github.com/PiSugar/PiSugar/wiki/PiSugar-3-Series)
* From the PiSugar Power Manager:
  * Configure "Single Tap" to custom shell.  Enter the following: 
    > sudo python /home/pi/camera.py
  * Configure long tap for shutdown
  * Set a safe shutdown threshold that works for your needs (I use 5%)
* [Configure Onboard RTC](https://github.com/PiSugar/PiSugar/wiki/PiSugar-3-Series#rtc-on-board)