from __future__ import absolute_import

import time

from .. import settings
from .arduino import Pin


class Floppy(object):

    """
    Represents a floppy drive connected to the Arduino

    """

    def __init__(self, id, step_pin_number, direction_pin_number):
        """
        Initializes the Floppy Drive

        """
        self.id = id
        self.step_pin = Pin(step_pin_number)
        self.direction_pin = Pin(direction_pin_number)

    def drive(self, direction, cycles, speed=settings.DEFAULT_SPEED):
        """
        Steps the motor a specified number of times in any direction

        """
        if speed > settings.MAX_SPEED:
            raise Exception("Fatal Error. Tried to drive board %s at %s Hz. This exceeds the maximum rate of %s Hz" % (self.id, speed, settings.MAX_SPEED))

        self.direction_pin.set_state(direction)
        for x in xrange(cycles):
            print "STEPPING DRIVE %s IN DIRECTION %s" % (self.id, direction)
            self.step_pin.pulse()
            time.sleep(float(1) / speed)


class FloppyArray(object):

    """
    Represents the array of floppy drives connected

    """

    def __init__(self):
        """
        Initializes the array

        """
        self.floppy_drives = []
        for x in xrange(2, (settings.FLOPPY_DRIVE_COUNT * 2) + 2, 2):
            self.floppy_drives.append(Floppy(len(self.floppy_drives), x, x + 1))
