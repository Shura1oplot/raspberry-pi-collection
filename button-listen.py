#!/usr/bin/env python

import sys
from time import time, sleep
import RPi.GPIO as GPIO


def main(argv=sys.argv):
    channel = int(argv[1])
    GPIO.setmode(GPIO.BCM)

    try:
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        ts = 0

        while True:
            GPIO.wait_for_edge(channel, GPIO.BOTH)

            if time() - ts <= 0.2:
                continue
            
            sleep(0.01)
            print "{}:{}".format(channel, GPIO.input(channel))
            sys.stdout.flush()
            ts = time()
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    sys.exit(main())
