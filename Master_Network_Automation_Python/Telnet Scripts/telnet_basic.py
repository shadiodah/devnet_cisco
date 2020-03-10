import getpass
import telnetlib


#your device ip (telnet server must be running)
host = '10.10.10.5'
user = 'cisco'
password = 'cisco'
#if you don't want a hardcoaded password use:
#passsword = getpass.getpass()

tn = telnetlib.Telnet(host)

#read until the bytes string Username appears
tn.read_until(b'Username: ')
#send the user as bytes. Ascii encoding is the default.
#always send also \n (new line, the enter key)
tn.write(user.encode('ascii') + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode('ascii')+b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n')

#each command should be sent as bytes
#the following 2 lines are equivalent
#tn.write(b'terminal length 0\n')
tn.write('terminal length 0\n'.encode())
tn.write(b'show version' + b'\n')
tn.write(b'configure terminal\n')
tn.write(b'end\n')
tn.write(b'exit\n')

line=tn.read_all().decode('ascii')
print(line)


