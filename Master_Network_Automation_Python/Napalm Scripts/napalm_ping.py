from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'andrei', 'cisco', optional_args=optional_args)
ios.open()
#start your code


output = ios.ping(destination='10.1.1.20', count=2, source='1.1.1.1')
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)

#end your code
ios.close()