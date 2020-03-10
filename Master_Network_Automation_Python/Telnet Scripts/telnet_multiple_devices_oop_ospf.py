import telnet_refactor_oop as tn_oop
#in this example we are importing and using the module defined (telnet_refactor_oop) as tn_oop

if __name__ == "__main__":
   #open # and process the file that contains IPs
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
        router1 = tn_oop.Device(element[0], 'cisco', 'cisco')
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

