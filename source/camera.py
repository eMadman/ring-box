#!/usr/bin/python3
import time
import os
import board
import neopixel


from picamera2 import Picamera2
from libcamera import controls

picam2 = Picamera2()
picam2.configure("still")
picam2.start()

#Define neopixel on Pin D18, 1 pixel
pixels = neopixel.NeoPixel(board.D18, 1)

# Give time for camera to settle
time.sleep(1)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast, "AeEnable": True, "AwbEnable": True, "FrameRate": 1.0})
#1s delay to allow AF/AWB to settle again
time.sleep(1)

# Capture 5 images.  2 second countdown between each image
start_time = time.time()

# Variable timestr with current datetime
timestr = time.strftime("%Y%m%d-%H%M%S")


# Loop until 5 images are captured
for i in range(1,6):
    # Neopixel countdown: Red 1s, Yellow 1s, White - then take pic and turn off neopixel
    pixels.fill((40,0,0))
    time.sleep(1)
    pixels.fill((30,30,0))
    time.sleep(1)
    pixels.fill((0,40,0))

    r = picam2.capture_request()

    pixels.fill((0,0,0))

    # Start with the original filename
    filename = f"/home/pi/{timestr}_image{i}.jpg"

    # Save the photo with the unique filename
    r.save("main", filename)
    r.release()
    print(f"Captured image {i} at {time.time() - start_time:.2f}s")


picam2.stop()


