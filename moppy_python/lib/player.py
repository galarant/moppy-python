from __future__ import absolute_import

import copy

from mido.midifiles import MidiFile

from . import floppy, utils


class MidiPlayer(object):

    """
    This is the object that will send MIDI files to the floppy array for playback

    """

    def __init__(self, midi_filename, arduino, floppy_array):
        """
        Creates and initializes the object

        """
        self.arduino = arduino
        self.midi_file = MidiFile(midi_filename)
        self.floppy_array = floppy_array

    def play(self):
        """
        Plays the midi file on the floppy array. Currently this is just a blocking call.

        """
        channel_map = {}
        mapped_drives = 0
        floppies_per_track = max(len(self.floppy_array) / len([t for t in self.midi_file.tracks if len(t) > 20]), 1)
        for message in self.midi_file.play():
            try:
                print message

                if message.channel in channel_map:
                    drives = channel_map[message.channel]
                else:
                    drives = []
                    for x in xrange(floppies_per_track):
                        drives.append(self.floppy_array[mapped_drives])
                        mapped_drives += 1

                    channel_map[message.channel] = drives

                if message.type == 'note_on':
                    note = max(0, message.note)
                    for drive in drives:
                        drive.play_note(note, is_midi=True)
                elif message.type == 'note_off':
                    for drive in drives:
                        drive.play_note(0)
            except IndexError:
                pass  # sorry brah. MIDI file has more channels than you can handle
            except AttributeError:
                pass  # whateverz
        utils.reset(self.arduino)
