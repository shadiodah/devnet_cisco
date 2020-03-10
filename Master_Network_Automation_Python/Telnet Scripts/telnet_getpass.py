import telnetlib
import getpass

host = '192.168.122.10'
user = input('Enter the username:')
#it will ask for the password without echoing it at the console
#the script must be run at the console and not in PyCharm or IDLE
#password = 'cisco'
password = getpass.getpass('Enter the password:')

tn = telnetlib.Telnet(host)
tn.read_until(b'Username: ')
tn.write(user.encode() + b'\n')

tn.read_until(b'Password: ')
tn.write(password.encode() + b'\n')

tn.write(b'enable\n')
tn.write(b'cisco\n') #this is the enable password
tn.write(b'terminal length 0\n') #this command is necessary to disable paging
tn.write(b'sh running-config\n')
tn.write(b'exit\n')
result = tn.read_all().decode()
print(result)

