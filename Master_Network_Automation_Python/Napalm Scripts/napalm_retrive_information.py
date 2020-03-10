from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'andrei', 'cisco', optional_args=optional_args)
ios.open()
#start your code

#output = ios.get_facts()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)


#output = ios.get_arp_table()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

# output = ios.get_interfaces()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

# output = ios.get_interfaces_counters()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)


# output = ios.get_interfaces_ip()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)


# output = ios.get_bgp_neighbors()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

output = ios.get_users()
dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)


#end your code
ios.close()