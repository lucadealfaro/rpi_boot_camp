# Image acquisition loop.
# BSD License.
# Luca de Alfaro, 2016

import os
import picamera
import time

IMG_FILE = '/ramfs/img.jpg'
TMP_FILE = '/ramfs/tmp.jpg'

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 30
    time.sleep(2)
    camera.start_preview()
    while True:
        # Picture acquisition loop.
        camera.capture(TMP_FILE, use_video_port=True)
        # Copies the file into place.
        os.rename(TMP_FILE, IMG_FILE)
