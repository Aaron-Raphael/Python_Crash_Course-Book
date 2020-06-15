# sets are used to store produce non repeted items

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# using set inn loop to avoid repeated values in dict
print('languages listed :')
for val in set(favorite_languages.values()):
    print('\t',val)