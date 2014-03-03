from __future__ import absolute_import

from unittest import TestCase
from nose.tools import eq_, ok_, with_setup
from pprint import pprint

import serial
import time

from Arduino import Arduino

from . import settings
from .lib import floppy


REQUIRED_SETTINGS = ('ARDUINO_BAUD_RATE',
                     'FLOPPY_DRIVE_COUNT',
                     'PULSE_WIDTH',
                     'DEFAULT_SPEED',
                     'MAX_SPEED')


class MoppyTest(TestCase):

    def setUp(self):
        """
        Ensure that settings are properly configured

        """
        for required_setting in REQUIRED_SETTINGS:
            if not hasattr(settings, required_setting):
                raise Exception('Need to set in moppy_project/settings.py in order to run the test suite' % required_setting)

        self.floppy_array = floppy.FloppyArray()

    def tearDown(self):
        """
        Reset motor positions and pins

        """
        for floppy_drive in self.floppy_array.floppy_drives:
            floppy_drive.step_pin.set_state(0)
            floppy_drive.direction_pin.set_state(0)

    def test_motors(self):
        """
        Tests that the motors are receiving pulses and responding properly

        """
        for floppy_drive in self.floppy_array.floppy_drives:
            floppy_drive.drive(direction=1, cycles=10)
            floppy_drive.drive(direction=0, cycles=10)
