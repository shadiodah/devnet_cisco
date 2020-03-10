import serial
import sys
import time
import re


def open_serial(port='com3', baudrate=9600):
    """Open and return a serial connection."""
    con = serial.Serial(port, baudrate, parity='N', stopbits=1, bytesize=8, timeout=8)
    if con.isOpen():
        return con
    else:
        return False


def run_command(con, cmd='\n', sleep=2):
    """Execute a command on serial connection."""
    if cmd != '\n':
        print('Sending command: ' + cmd)
    con.write(cmd.encode() + b'\n')
    time.sleep(sleep)	#mandatory


def read_from_console(con):
    """Read from serial and return string."""
    bytesToBeRead = con.inWaiting()
    if bytesToBeRead:
        return con.read(bytesToBeRead).decode()
    else:
        return 'Nothing to read from serial'


def check_initial_configuration_dialog(console):
    run_command(console, '\n')
    prompt = read_from_console(console)
    if 'Would you like to enter the initial configuration dialog?' in prompt:
        run_command(console, 'no')
        time.sleep(15)
        run_command(console, '\r\n')

        return True
    else:
        return False


console = open_serial()
check_initial_configuration_dialog(console)
with open('serial.txt', 'rt') as f:
    commands = f.readlines()

for cmd in commands:
    run_command(console, cmd)
