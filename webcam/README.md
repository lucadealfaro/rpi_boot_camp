# Webcam Boot Camp
Luca de Alfaro, 2016
 
In this boot camp, we will transform our RPI into a web-viewable webcam. Obviously, you need to have installed the [camera module](https://www.raspberrypi.org/products/camera-module/) on your RPI for this to work; see [these instructions](https://www.raspberrypi.org/help/camera-module-setup/). To start, go to the webcam directory:

    cd webcam

### If you have an 8MB, v2 camera

The camera firmware was shipped with a bug that mirrors the images, left-to-right. Images are easy to fix (e.g., using PIL, the Python imaging library), but movies are harder. If you wish to correct the image mirroring, proceed as follows (see [here](https://www.raspberrypi.org/forums/viewtopic.php?f=43&t=145980) for an explanation):

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

    sudo cp scripts/ramfs /etc/init.d
    sudo chown root /etc/init.d/ramfs
    sudo chmod u+x /etc/init.d/ramfs
    sudo update-rc.d ramfs defaults
    
This will create a 200MB RAM filesystem and mount it at /ramfs whenever the rpi boots. Before proceeding, mount it manually without rebooting via:

    /etc/init.d/ramfs start
    
### Image acquisition loop    

To start the image acquisition loop, we first need to install the picamera Python package, which enables camera access from python. 

    sudo apt-get install python-picamera
    
Then, you can run the image acquisition code by hand:

    python image_acquisition/image_loop.py
    
Good.  Now, to keep it up and running, you can either do:

    python image_acquisition/image_loop.py &
    
and then kill it if needed with

    killall /usr/bin/python
    
or else, you can also start that via an init script:

    sudo cp scripts/camcam /etc/init.d
    sudo chown root /etc/init.d/camcam
    sudo chmod u+x /etc/init.d/camcam
    sudo update-rc.d camcam defaults
    sudo /etc/init.d/camcam start
    
### Visualization

We assume that you got the image acquisition loop above working. To visualize the images, we are going to use the [web2py](http://www.web2py.com) web framework.  Let's get the code:

    cd ~/rpi_boot_camp
    wget http://www.web2py.com/examples/static/web2py_src.zip
    unzip web2py_src.zip

A web2py application can consist of multiple apps; see the [web2py book](http://book.web2py.com) for more information.  We now need to link the viewcam app to the web2py server.

    ln -s 

 

 
### Starting the web server

You can start the web server man
