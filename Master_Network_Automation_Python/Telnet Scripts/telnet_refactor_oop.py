class Device:
    """
    This is the constructor. There are 4 object's attributes: ip, username, password and connection
    """
    def __init__(self, ip, username, password, connection=None):
        self.ip = ip
        self.username = username
        self.password = password
        self.connection = connection

    def connect(self):
        """
        Connects to the device
        """
        import telnetlib
        self.connection = telnetlib.Telnet(self.ip)

    def authenticate(self):
        """
        Authenticates to the device.
        """
        self.connection.read_until(b'Username: ')
        self.connection.write(self.username.encode() + b'\n')
        self.connection.read_until(b'Password: ')
        self.connection.write(self.password.encode() + b'\n')

    def execute(self, command):
        self.connection.write(command.encode() + b'\n')

    def show(self):
        output = self.connection.read_all().decode('utf-8')
        return output



if __name__ == "__main__":
   #open and process the file that contains IPs
    with open('devices.txt', 'r') as f:
        d = f.read().splitlines()

    ip = list()
    for item in d:
        x = item.split(':')
        ip.append(tuple(x))

    #ip list is a list of tuples
    #print('ip list:', ip)
    #iterating through the ip list and setting the loopback int and ospf for each element
    for element in ip:
        router1 = Device(element[0], 'cisco', 'cisco')
        router1.connect()
        router1.authenticate()
        router1.execute('enable')
        router1.execute('cisco')  #this is the enable password
        router1.execute('terminal length 0') #this disables paging, necessary for show commands
        router1.execute('configure terminal')
        router1.execute('interface loopback 0')
        #the loopback interface is at index 1
        router1.execute('ip address ' + str(element[1]) + ' 255.255.255.255')
        router1.execute('exit')
        router1.execute('router ospf 1')
        router1.execute('network 0.0.0.0 0.0.0.0 area 0')
        router1.execute('end')
        router1.execute('show ip protocols')
        router1.execute('exit')
        output = router1.show()
        print(output)
