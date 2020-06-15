# the vavourite lang are stored as list values in dictionary
favorite_languages = {    
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

# looping through dict
for name,fav_lang in favorite_languages.items():
    print('favourite languages of ' + name + ' are :')
    # looping through list
    for lang in fav_lang:
        print('\t',lang)