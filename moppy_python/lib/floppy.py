from __future__ import absolute_import

from .. import settings


class Floppy(object):

    """
    Represents a floppy drive connected to the Arduino

    """

    def __init__(self, id, control_pin, direction_pin, arduino):
        """
        Initializes the Floppy Drive

        """
        self.id = id
        self.control_pin = control_pin
        self.direction_pin = direction_pin
        self.arduino = arduino

    def play_note(self, note):
        """
        Plays a note

        """
        note = note / settings.ARDUINO_RESOLUTION
        self.arduino.write(chr(self.control_pin))
        self.arduino.write(chr(note >> 8))
        self.arduino.write(chr(note % 256))

    def rest(self):
        """
        Plays a rest

        """
        self.arduino.write(chr(self.control_pin))
        self.arduino.write(chr(0))
        self.arduino.write(chr(0))

def initialize_floppy_array(num_drives, arduino):
    """
    Sets up an inital array of floppy drives assuming the standard pin wiring

    """
    floppy_drives = []
    for x in xrange(2, (num_drives * 2) + 2, 2):
        floppy_drives.append(Floppy(len(floppy_drives), x, x + 1, arduino))

    return floppy_drives
