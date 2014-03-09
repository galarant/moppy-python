import glob
import serial
import platform

# A function that tries to list serial ports on most common platforms


def list_serial_ports():
    system_name = platform.system()
    if system_name == "Windows":
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append(i)
                s.close()
            except serial.SerialException:
                pass
        return available
    elif system_name == "Darwin":
        # Mac
        return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
    else:
        # Assume Linux or something else
        return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')


def reset(arduino):
    """
    Sends a special byte sequence that resets all drives

    """
    arduino.write(chr(100))
    arduino.write(chr(100))
    arduino.write(chr(100))
