from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'andrei', 'cisco', optional_args=optional_args)
ios.open()
#start your code

output = ios.get_arp_table()
# for item in output:
#     print(item)


dump = json.dumps(output, sort_keys=True, indent=4)
#print(dump)

with open('arp.txt', 'w') as f:
    f.write(dump)

#end your code
ios.close()