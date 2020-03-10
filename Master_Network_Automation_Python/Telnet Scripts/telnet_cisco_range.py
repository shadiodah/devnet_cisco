import telnetlib
import time

#devices.txt contains an IP address on each line
with open('mydevices.txt','r') as f:
    ips = f.read().splitlines()

#print(ips)
#alternatively we can use a list
#ips=['10.1.1.10','10.1.1.20','10.1.1.30']


user = 'cisco'
password = 'cisco'
#iterate through the list of devices and execute the same commands
for ip in ips:
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')

    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')

    tn.write(b'enable\n')
    tn.write(b'cisco\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'show run' + b'\n\n')  # ???
    time.sleep(3)
    tn.write(b'show ip int brief' + b'\n\n')  # ???
  #  tn.write(b'configure terminal\n')
  #  tn.write(b'end\n')
    tn.write(b'exit\n')
    line = tn.read_all().decode('ascii')
    print(line)