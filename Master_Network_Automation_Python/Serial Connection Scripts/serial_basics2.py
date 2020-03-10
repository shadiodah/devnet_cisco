import serial
import time
with serial.Serial(port='com3', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8) as console:
    if console.isOpen():
        print('Console successfully opened!')
        console.write(b'\n')
        time.sleep(1)
        console.write(b'enable\n')
        time.sleep(1)
        console.write(b'terminal length 0\n')
        time.sleep(1)
        console.write(b'show version\n')
        time.sleep(3)
        bytes_to_be_read = console.inWaiting()
        output = console.read(bytes_to_be_read)
        print(output.decode())
    else:
        print('Error opening the console connection')