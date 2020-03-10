from netmiko import ConnectHandler
from termcolor import cprint
"""
This script will check if the Router interface the user enters is enabled and if not it will enable it.
"""
with open('devices.txt') as f:
    file_content = f.read().splitlines()

devices = list()
for item in file_content:
    tmp = item.split(':')  #tmp is a list
    devices.append(tmp)

for device in devices:
    net_device = {
        'device_type': device[0],
        'ip': device[1],
        'username': device[2],
        'password': device[3],
        'port': 22,
        'secret': device[3],  # this is the enable password
        'verbose': True
    }

    net_connect = ConnectHandler(**net_device)

    prompter = net_connect.find_prompt()
    if '>' in prompter:
        net_connect.enable()

    interface = input('Enter the interface you want to enable:')
	
    #check the interface status
    output = net_connect.send_command('sh ip interface ' + interface)
    #print(output)

    #if an invalid interface has been entered
    if 'Invalid input' in output:
        print('You entered and invalid interface')
    else:
        lines = output.splitlines()
        #print(lines)
        first_line = output.splitlines()[0] #1st line of the sh ip interface command output
        cprint('-' * 45,'red')
        cprint(first_line,'red')
        cprint('-' * 45,'red')
        if not ' up ' in first_line:  #if the interface is not up
            cprint('The interface is down. Enabling the interface ...',attrs=['bold'])
            commands = ['interface ' + interface, 'no shut', 'exit' ]   #enabling the interface
            output = net_connect.send_config_set(commands)
            print(output)
            print('#' * 40)
            cprint('The interface has been enabled',attrs=['bold'])
        else:   #if the interface is already enabled
            cprint('Interface ' + interface + ' is already enabled',attrs=['bold'])
    print('#' * 40)
    net_connect.disconnect()

