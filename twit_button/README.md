# Twitter-Connected Button Boot Camp

In this boot camp we will construct a twitter and LED-connected button.
We start with some hardware magic.  This is the pinout of the RPI GPIO:

[Pinout](resources/physical-pin-numbers.png)

We are going to connect:

- A normally-open button between pins 39 and 40.  
- A 330 Ohm resistor and a LED between pins 

**Button.** Pin 34 is ground.  Pin 33 is a GPIO pin, and we will configure it to be an input, and to have a pull-up resistor programmed via software.  In this way, when the button is pushed, we will read 0 from GPIO pin 40, and we will read 1 otherwise. 

**LED.**  Pin 39 is ground.  Pin 40 is a GPIO pin, and we will configure it to be an output.  When we will write a 1 to it, the LED will light. 

Here is some [documentation on RPI GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/).  And here is [how it looks](resources/breadboard.jpg) on my breadboard.

## Button and LED

Let us first make the LED come up when the button is pressed for at least 1 second.
[Here is the code](button_and_led.py); please study it carefully.
You can use it via: 

    cd twit_button
    python button_and_led.py

Note how, every time a button press is detected, the LED turns on for 0.5 seconds. 

## Twitter connection

Next, we are going to develop an application where, at each button press, we post an update to twitter.  Just because!  This could be a useful kind of doorbell, after all.  Plus, this is a good example of how to get a device "do stuff" with the internet.  First, we need to install some software. First the excellent [requests](http://docs.python-requests.org/en/master/user/quickstart/) package to make requests:

    sudo apt-get install python-requests
    
And the excellent simple Twitter API written by Rakshit Agrawal (do this from the twit_button directory):

    git clone https://github.com/rakshit-agrawal/python-twitter-apps.git
    touch python-twitter-apps/__init__.py

Follow [these instructions](https://github.com/rakshit-agrawal/python-twitter-apps) to create a Twitter account (if you don't have one already), and an App, obtaining the authentication parameters.
Then add them as follows to the configuration file:

    cp credentials.example.json credentials.json
    nano credentials.json

and complete the information there. 

    
