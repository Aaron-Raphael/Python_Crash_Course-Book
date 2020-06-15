# defining multiple dicts
alien_0 = {'color': 'green', 
           'points': 5}

alien_1 = {'color': 'yellow',
           'points': 10}

alien_2 = {'color': 'red',
           'points': 15}

# nesting dicts in a list
aliens = [alien_0 , alien_1 , alien_2]

# looping through list printing the res dict
for alien in aliens:
    print(alien)