import picamera
import time
import os
from PIL import Image
filename = '/ramfs/qr.jpg'
sx, sy = 2592, 1955
with picamera.PiCamera() as camera:
    # camera.resolution=(sx,sy) 
    camera.hflip = True
    while True:
        camera.capture('/ramfs/picamera.jpg')
        img = Image.open('/ramfs/picamera.jpg')
        # img = img.crop((sx * 1 / 3, sy * 1 / 3, sx * 2 / 3, sy * 2 / 3))
        img.save('/ramfs/picamera.jpg')
        os.system('cp /ramfs/picamera.jpg %s' % filename)
        time.sleep(0.1)
        
