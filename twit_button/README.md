# Twitter-Connected Button Boot Camp

In this boot camp we will construct a twitter and LED-connected button.
We start with some hardware magic.  This is the pinout of the RPI GPIO:

[Pinout](resources/physical-pin-numbers.png)

We are going to connect:

- A normally-open button between pins 39 and 40.  
- A 330 Ohm resistor and a LED between pins 

**Button.** Pin 39 is ground.  Pin 40 is a GPIO pin, and we will configure it to be an input, and to have a pull-up resistor programmed via software.  In this way, when the button is pushed, we will read 0 from GPIO pin 40, and we will read 1 otherwise. 

**LED.**  Pin 34 is ground.  Pin 33 is a GPIO pin, and we will configure it to be an output.  When we will write a 1 to it, the LED will light. 

Here is some [documentation on RPI GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/).

## Button and LED

Let us first make the LED come up when the button is pressed for at least 1 second.
[Here is the code](button_and_led.py); please study it carefully.

## Twitter connection

Check out the excellent simple Twitter API written by Rakshit Agrawal:

    cd twit_button
    git clone https://github.com/rakshit-agrawal/python-twitter-apps.git
    
