# defining dict inside a dict:

# defining outer dict uders
users = {  
    # definning nested dict as  a value   
        'aeinstein': {
                    'first': 'albert',
                    'last': 'einstein',        
                    'location': 'princeton',        
                     },

        'mcurie': {        
                    'first': 'marie',        
                    'last': 'curie',        
                    'location': 'paris',        
                    },
    }

for name,details in users.items():
    print('Name is ' + name + '\n details :')
    for key,val in details.items():
        print('\t' + key + ':' +  val)

for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())