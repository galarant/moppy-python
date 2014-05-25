from __future__ import absolute_import
from unittest import TestCase
from nose.tools import eq_, ok_, with_setup

import os
import time
import serial

from . import settings
from .lib import floppy, utils, player


REQUIRED_SETTINGS = ('DEFAULT_SERIAL_PORT',
                     'ARDUINO_BAUD_RATE',
                     'ARDUINO_RESOLUTION',
                     'FLOPPY_DRIVE_COUNT',
                     'SEMITONE_SCALE',
                     'MAJOR_SCALE',
                     )


class SoftwareTest(TestCase):

    def setUp(self):
        """
        Ensure that settings are properly configured

        """
        for required_setting in REQUIRED_SETTINGS:
            if not hasattr(settings, required_setting):
                raise Exception('Need to set in moppy_project/settings.py in order to run the test suite' % required_setting)

    def test_detect_serial_ports(self):
        """
        Test that serial ports are detected

        """
        serial_ports = utils.list_serial_ports()
        ok_(serial_ports)
        ok_(settings.DEFAULT_SERIAL_PORT in serial_ports)


class HardwareTest(TestCase):

    def setUp(self):
        """
        Ensure that settings are properly configured and set up arduino

        """
        for required_setting in REQUIRED_SETTINGS:
            if not hasattr(settings, required_setting):
                raise Exception('Need to set in moppy_project/settings.py in order to run the test suite' % required_setting)

        self.arduino = serial.Serial(settings.DEFAULT_SERIAL_PORT, settings.ARDUINO_BAUD_RATE)
        self.floppy_drives = floppy.initialize_floppy_array(settings.FLOPPY_DRIVE_COUNT, self.arduino)
        print "SLEEPING FOR ARDUINO INITIALIZATION"
        time.sleep(5.0)

    def tearDown(self):
        """
        Reset motor positions and pins

        """
        print "RESETTING FLOPPIES"
        utils.reset(self.arduino)

    def test_floppy_drives(self):
        for floppy_drive in self.floppy_drives:
            for note in settings.MAJOR_SCALE:
                print "SENDING NOTE %s TO FLOPPY %s" % (note, floppy_drive.id)
                floppy_drive.play_note(note)
                time.sleep(0.125)
            print "RESTING ON FLOPPY %s" % (floppy_drive.id)
            floppy_drive.rest()

        for note in settings.MAJOR_SCALE:
            print "SENDING NOTE %s TO ALL DRIVES SIMULTANEOUSLY" % note
            for floppy_drive in self.floppy_drives:
                floppy_drive.play_note(note)
            time.sleep(0.125)
        utils.reset(self.arduino)

    def test_song(self):
        """
        Test that we can play a song

        """
        midi_filename = os.path.dirname(os.path.abspath(__file__)) + '/../midi/Zelda.mid'
        midi_player = player.MidiPlayer(midi_filename, self.arduino, self.floppy_drives)
        midi_player.play()
