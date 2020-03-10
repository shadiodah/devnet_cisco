from netmiko import ConnectHandler
"""
This script will check if the Router interface the user enters is enabled and if not it will enable it.
"""

cisco_device = {
        'device_type': 'cisco_ios',     #device type from https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py
        'ip': '10.1.1.20',
        'username': 'u1',
        'password': 'cisco',
        'port': 22,             #optional, default 22
        'secret': 'cisco',      #optional, default ''
        'verbose': True         #optional, default False
        }

net_connect = ConnectHandler(**cisco_device)
prompter = net_connect.find_prompt()
if '>' in prompter:
        net_connect.enable()


interface = input('Enter the enterface you want to enable:')

#check the interface status
output = net_connect.send_command('sh ip interface ' + interface)

#if an invalid interface has been entered
if 'Invalid input detected' in output:
    print('You entered and invalid interface')
else:
    first_line = output.splitlines()[0] #1st line of the sh ip interface command output
    print(first_line)
    if not 'up' in first_line:  #if the interface is not up
        print('The interface is down. Enabling the interface ...')
        commands = ['interface ' + interface, 'no shut', 'exit' ]   #enabling the interface
        output = net_connect.send_config_set(commands)
        print(output)
        print('#' * 40)
        print('The interface has beed enabled')
    else:   #if the interface is already enabled
        print('Interface ' + interface + ' is already enabled')



net_connect.disconnect()

