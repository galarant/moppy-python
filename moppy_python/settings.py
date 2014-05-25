# These values are highly environment-dependent
# Make sure to verify them for your own system before running the test suite

DEFAULT_SERIAL_PORT = '/dev/tty.usbmodem1411'
ARDUINO_BAUD_RATE = 9600
ARDUINO_RESOLUTION = 40  # Microsecond resolution for notes
FLOPPY_DRIVE_COUNT = 8

SEMITONE_SCALE = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # unused
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # unused
    30578, 28861, 27242, 25713, 24270, 22909, 21622, 20409, 19263, 18182, 17161, 16198,  # C1 - B1
    15289, 14436, 13621, 12856, 12135, 11454, 10811, 10205, 9632, 9091, 8581, 8099,  # C2 - B2
    7645, 7218, 6811, 6428, 6068, 5727, 5406, 5103, 4816, 4546, 4291, 4050,  # C3 - B3
    3823, 3609, 3406, 3214, 3034, 2864, 2703, 2552, 2408, 2273, 2146, 2025,  # C4 - B4
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # unused
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # unused
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  # unused
]

MAJOR_SCALE = [
    7645, 6811, 6068, 5727, 5103, 4546, 4050, 3823,  # C3 - C4 used mainly for testing
]
