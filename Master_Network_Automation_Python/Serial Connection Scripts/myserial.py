import serial
import time

def open_console(port='com3', boudrate = 9600):
    console = serial.Serial(port='com3', baudrate=9600, parity='N', stopbits=1, bytesize=8, timeout=8)
    if console.isOpen():
        return console
    else:
        return False


def run_command(console, cmd='\n', sleep=2):
    print('Sending command: ' + cmd)
    console.write(cmd.encode() + b'\n')
    time.sleep(sleep)


def read_from_console(console):
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        return output.decode()
    else:
        return False


def check_initial_configuration_dialog(console):
    run_command(console, '\n')
    prompt = read_from_console(console)
    if 'Would you like to enter the initial configuration dialog?' in prompt:
        run_command(console,'no', 15)
        run_command(console, '\r\n')
        return True
    else:
        return False



