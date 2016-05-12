import datetime
import json
import RPi.GPIO as GPIO
import time
from twitter.twitter import Twitter

# There are two modes of using GPIO pins: using board numbering,
# or using chip numbering.  We use board numbering here.
GPIO.setmode(GPIO.BOARD)

# Which pins we use how.
PIN_OUT = 40
PIN_IN = 33

# Sets pin 40 to input with pull-up resistor.
GPIO.setup(PIN_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Sets pin 33 as output.
GPIO.setup(PIN_OUT, GPIO.OUT)
GPIO.output(PIN_OUT, False)

# We need to read in our twitter keys.
twitter_info = json.load(open('credentials.json'))
twitter_access = twitter_info['access']
twitter_username = twitter_info['username']

# This is the twitting function.
def twit():
    t = Twitter(**twitter_access)
    t.post_twit("I have been pressed into service at %s" % datetime.datetime.now().isoformat())

# This is the callback for when a button press has been detected.
def button_press(channel):
    print "Button press on %r" % channel
    # We flash the LED ON for half a second.
    GPIO.output(PIN_OUT, True)
    # Here is the novelty: we do the twitter call!
    twit()
    GPIO.output(PIN_OUT, False)

# We attach the callback to the button with a debounce time of 200ms.
GPIO.add_event_detect(PIN_IN, GPIO.FALLING, callback=button_press, bouncetime=200)

# That's all, folks.
# We need to sleep forever.
while True:
    time.sleep(1.0)

