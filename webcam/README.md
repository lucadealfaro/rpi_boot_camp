# Webcam Boot Camp
Luca de Alfaro, 2016
 
In this boot camp, we will transform our RPI into a web-viewable webcam. 

### If you have an 8MB, v2 camera

The camera firmware was shipped with a bug that mirrors the images, left-to-right. Images are easy to fix (e.g., using PIL, the Python imaging library), but movies are harder. If you wish to correct the image mirroring, proceed as follows:

    sudo apt-get update
    sudo apt-get upgrade
    sudo rpi-update

## Overview

To create our webcam, we will need three steps:

- Create a RAM file system, to avoid writing too frequently to the SD card. 
- Continuously read images, and write them to the SD card RAM file system.
- Serve the images in a webapp.

### Creating the RAM file system

The webcam consists of two pieces of code.  The first piece will continuously read the webcam, and store an image on the filesystem.  The second piece will serve a webpage, that will continuously read the image from the filesystem and thus display an always-updating image. 

Flash memory can be written only a finite, and not very large, amount of times before it fails. A solution to this problem is to use a filesystem in RAM.  To this end do:

    cd webcam
    cp scripts/ramfs /etc/init.d
    sudo update-rc.d ramfs defaults
    
This will create a 50MB RAM filesystem and mount it at /ramfs whenever the rpi boots. You can mount it manually without rebooting via:

    /etc/init.d/ramfs start
    
### Image acquisition loop    

To start the image acquisition loop, 

### Starting the web server

You can start the web server man
