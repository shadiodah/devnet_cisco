from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.1.1.10', 'admin', 'cisco', optional_args=optional_args)
ios.open()

ios.load_replace_candidate(filename='config.txt')


diff = ios.compare_config()
#print(diff)
if len(diff):
    print(diff)
    print('Commit changes...')
    ios.commit_config()
    print('Done')
else:
    print('No changes required')
    ios.discard_config()


answer = input('Rollback config?')
if answer == 'yes':
    ios.rollback()


ios.close()