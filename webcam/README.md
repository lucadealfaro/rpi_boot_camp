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

A web2py application can consist of multiple apps; see the [web2py book](http://www.web2py.com/book) for more information.  We now need to link the viewcam app to the web2py server.

    ln -s ../../webcam/viewcam web2py/applications/
    
If you think the ../.. above doesn't make sense, so do I. But someone else sometime ago must have thought otherwise. Oh well. You can now start web2py manually: 

    python web2py/web2py.py -e -a banana -i 0.0.0.0 -p 8888
        
If the IP address of your RPI is (for example) 192.168.1.163, point your browser to the URL [http://192.168.1.163:8888/viewcam/](http://192.168.1.163:8888/viewcam/).  You should see the image periodically (and fast) updating.  Congratulations! 

If you now want your webcam to start automatically at boot, you can do:

    cd webcam
    sudo cp scripts/web2py /etc/init.d
    sudo chown root /etc/init.d/web2py
    sudo chmod u+x /etc/init.d/web2py
    sudo update-rc.d web2py defaults
    sudo /etc/init.d/web2py start

**Note:** *This is not secure.* You have started on the RPI a web server with password "banana".  At the very least, change this password (*both* in the script above, and in scripts/web2py) to some password of your choice, and reinstall the auto-run script via:

    sudo cp scripts/web2py /etc/init.d
    sudo update-rc.d web2py defaults

### Next steps

The code that produces the information in the web page is in webcam/viewcam/controllers/default.py , and the code that produces the HTML page is in webcam/viewcam/views/default/index.html . 
    
- You can learn more about the [Python interface to the RPI camera](https://picamera.readthedocs.io/en/release-1.10/).
- You can learn more about [Web2Py](http://www.web2py.com/book).

Happy coding!
