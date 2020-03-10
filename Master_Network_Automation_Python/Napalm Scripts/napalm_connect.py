from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'andrei', 'cisco', optional_args=optional_args)
ios.open()

#show all methods available
print(dir(ios))

ios.close()