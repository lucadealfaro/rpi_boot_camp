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
    t.post_tweet("I have been pressed into service at %s" % datetime.datetime.now().isoformat())

# We debounce ourselves, since the standard debouncing leaves much to be desired.
num_consecutive = 0
while True:
    if GPIO.input(PIN_IN):
        num_consecutive = 0
    else:
        num_consecutive += 1
        if num_consecutive > 2:
            num_consecutive = 0
            GPIO.output(PIN_OUT, True)
            twit()
            GPIO.output(PIN_OUT, False)
    time.sleep(0.5)

