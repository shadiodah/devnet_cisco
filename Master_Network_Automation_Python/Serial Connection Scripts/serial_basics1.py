import serial
import time

with serial.Serial(port='com3', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8) as console:
    if console.isOpen():
        print('Serial is Opened')

        console.write(b'\n')
        time.sleep(1)
        console.write(b'ena\n')
        time.sleep(1)
        console.write(b'terminal length 0\n')
        time.sleep(1)
        console.write(b'sh version\n')

        time.sleep(3)

        bytes_to_be_read = console.inWaiting()
        output = console.read(bytes_to_be_read)
        print(output.decode())