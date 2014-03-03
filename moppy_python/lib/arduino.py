from __future__ import absolute_import

import time
from Arduino import Arduino

from ..import settings

class Pin(object):
    """
    Represents a pin on the Arduino board

    """

    def __init__(self, pin_number):
        """
        Initializes the pin

        """
        self.board = Arduino(str(settings.ARDUINO_BAUD_RATE), port=settings.DEFAULT_SERIAL_PORT)
        self.pin_number = pin_number

    def get_state(self):
        """
        Get the state of the pin

        """
        return self.board.digitalRead(self.pin_number)

    def set_state(self, high_low):
        """
        Set the state of the pin

        """
        if high_low:
            self.board.digitalWrite(self.pin_number, "HIGH")
        else:
            self.board.digitalWrite(self.pin_number, "LOW")

    def pulse(self):
        """
        Sends a single pulse to a pin

        """
        if self.get_state():
            self.set_state(0)

        self.set_state(1)
        time.sleep(settings.PULSE_WIDTH)
        self.set_state(0)
