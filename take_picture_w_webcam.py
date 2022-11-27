#!/usr/bin/env python3

# Python 3.9.5

# take_picture_w_webcam.py

# Install fswebcam on your Raspberry Pi previously: sudo apt install fswebcam
# Be sure to plug in the camera. Check the status with: lsusb

# Dependency
import os

path = 'home/user/images/'
# The command has several options, like -r or --no-banner:
command = f'fswebcam -r 1280x720 --no-banner {path}image1.jpg'

os.system(command) # Executes the command and the camera will take a picture
