from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'} #cisco is the enable password
ios = driver('10.10.10.1', 'admin', 'cisco', optional_args=optional_args)
ios.open()

ios.load_merge_candidate('acl.txt')


diff = ios.compare_config()

if len(diff) > 0:
    print(diff)
    answer = input('Commit changes?<yes|no>')
    if answer == 'yes':
        print('Commit changes...')
        ios.commit_config()
        print('Done')
    else:
        print('No changes required')
        ios.discard_config()




ios.close()