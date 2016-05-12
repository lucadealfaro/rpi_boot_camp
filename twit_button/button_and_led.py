import RPi.GPIO as GPIO
import time

# There are two modes of using GPIO pins: using board numbering,
# or using chip numbering.  We use board numbering here.
GPIO.setmode(GPIO.BOARD)

# Sets pin 40 to input with pull-up resistor.
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Sets pin 33 as output.
GPIO.setup(33, GPIO.OUT)

# This is the callback for when a button press has been detected.
def button_press(channel):
    print "Button press on %r" % channel
    # We flash the LED ON for half a second.
    GPIO.output(33, True)
    time.sleep(0.5)
    GPIO.output(33, False)

# We attach the callback to the button with a debounce time of 200ms.
GPIO.add_event_detect(40, GPIO.FALLING, callback=button_press, bouncetime=200)

# That's all, folks.

