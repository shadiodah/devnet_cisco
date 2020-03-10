import telnetlib
import time
import getpass

#the list of devices we configure. there must ip connectivity to each device
#we must be able to connect to each device using telnet
#mydevices = ['10.1.1.10', '10.1.1.20', '10.1.1.30']
mydevices = ['192.168.122.10', '192.168.122.20']

for device in mydevices:
    user = 'cisco'
    #password = getpass.getpass() #ask for the user password without echoing it at the console
    password = 'cisco'
    # create a telnet object
    tn = telnetlib.Telnet(device)
    tn.read_until(b'Username: ')
    tn.write(user.encode() + b'\n')

    tn.read_until(b'Password: ')
    tn.write(password.encode() + b'\n')

    tn.write(b'enable\n')
    tn.write(b'cisco\n') #this is the enable password

    #create default route
    tn.write(b'configure terminal\n')
    tn.write(b'ip route 0.0.0.0 0.0.0.0 e0/0 10.1.1.2\n')
    tn.write(b'end\n')

    tn.write(b'terminal length 0\n')
    tn.write(b'sh ip route\n')
    tn.write(b'exit\n')
    #exit command is mandatory to be able read using read_all()
    result = tn.read_all().decode()

    print(result)
    print('#####################################')
    time.sleep(1)

