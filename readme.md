<img src="/pictures/closed_box.jpg" alt="closed ring box" height="200"> <img src="/pictures/open_box.jpg" alt="open ring box" height="200">

# Camera Equipped Ring Box

The backstory here is that my partner dreamt of being proposed to in a photo booth.  Those are hard to find around town and I figured I could interpret the idea into something more interesting to me.

The idea of the camera in a ring box was born.  After some googling, I learned that it's not unique.  Commercial products exist that probably work much better from a usability and packaging standpoint. 

This falls firmly into DIY territory and I very much encourage remixing and improvements to the idea.  Please link back to this if you use it.  I want to know what you come up with and how you improve on it!

## Features
* Minimal hardware - only 2 screws and threaded inserts required for the hinge mechanism
* Integrated LED for camera countdown timer
* Excellent photo quality thanks to Pi Camera Module 3
* Onboard real time clock for file organization and naming
* Can operate on battery for several hours

## BOM
* Raspberry Pi Zero 2 W.  I used the Pi Zero W and it is woefully underpowered (see limitations below).  Get the faster board if it's in stock.
* [Pisugar 3](https://www.tindie.com/products/pisugar/pisugar-3-battery-for-raspberry-pi-zero/)
* Raspberry Pi Camera Module 3
* 150mm Pi Camera Module ribbon cable for Pi Zero W and Zero 2W
* 2x M3x8 BHCS Screws
* 2x M3x5x6 threaded inserts
* 4x M2 screws
* 1x Neopixel Module (WS2812B) - Optional
* Foam or other material to hold the ring
* Adhesive or magnet for PiSugar battery

## Assembly instructions
1. Install ribbon cable on the Raspberry Pi
2. Pi should snap into place into place into the enclosure.  Watch the orientation - there is a cutout for the ribbon cable
3. Insert buttons into enclosure
4. Carefully attach PiSugar 3 module to back of pi with screws included in packaging.  Take care that buttons don't fall out.  Ensure POGO pins have good contact with GPIO header.  
5. Tape or glue battery into enclosure in the available space
6. Snap bottom cover
7. Wire up NeoPixel onto GPIO headers.  Use the [Adafruit instructions](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring#powering-neopixels-from-raspberry-pi-without-level-shifting-3006456).  Due to lack of space, I clipped some pins and bent back the relevant pins so that I could use dupont connectors.  Soldering will provide a much better connection.  
<img src="/pictures/gpio.png" alt="gpio" height="200">
8. Glue neopixel onto diffuser and into pi_cover.stl
9. Thread ribbon cable through pi_cover.stl and snap cover into place
10. Screw camera module into camera_cover.stl
11. Install heatset inserts on lid
12. Screw lid onto main body with M3 screws
13. Thread ribbon cable through camera_cover.stl and attach the camera.  Snap cover into the lid
14. Cut foam to size and insert into ring cavity
15. Propose!

## Limitations 

My usage of the Pi Zero W instead of the Pi Zero 2 W led to some performance related challenges.  The first camera module I tested was the Arducam 64MP module.  The older generation of Pi simply could not keep up and would crash while using this module.  Pi Camera Module 3 works better but there are some delays in initializing the camera (approx 8 seconds between shutter button press and the LED countdown starting).  

I did not attempt video capture due to concerns around the Pi Zero W's performance with higher resolutions.

## Potential enhancements
I don't plan to pursue these enhancements, except perhaps an LCD picture frame in this form factor, but I think they represent potential future improvements of the concept:

* Replacement lid or addons to transform the box into an LCD picture frame for display purposes
* Wifi hotspot fallback through OS configuration to allow SSH into the device from outside of your home wifi network
* Video capture instead of photo capture
* Mechanisms of retrieving photos that are usable by non-technical people (web portal, for example)
* Sturdier hinges and panel snaps
* Shutter triggered by opening of lid

## Licensing
This project is licensed under the [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 license](LICENSE).

## References
This project would not be possible without the following reference material:

* [PiSugar3](https://github.com/PiSugar/PiSugar).  The case design was remixed from the PiSugar 3 enclosure.
* [Picamera2 Documentation](https://github.com/raspberrypi/picamera2) 3 which provided the necessary hints to get this code working.
* Adafruit's [NeoPixel on Raspberry Pi Tutorial](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview) 
* Microsoft's Bing Chat for helping me write and troubleshoot the python script







<img src="Pictures/Schwinn_IC4_MOD.png" alt="Hardware 2.0"/> 

[_^^@eMadman's IC4 model_](https://github.com/doudar/SmartSpin2k/tree/develop/Hardware/MODS/Case%20V2%20-%20Schwinn%20IC4%20Mod)
