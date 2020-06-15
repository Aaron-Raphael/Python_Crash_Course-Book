# dictionary is declared by key value pair in {}

person = {
    'name':'aaron',
    'age':19,
    'city':'cbe',
    'lang_2':'tamil'
    }

# looping through dictionary
for key in person: # for key in person.keys():
    print( key,'is',person[key])

# entering new key:value pair 
if 'school' not in person:
    sch_name = input('enter "school" value: ')
    person['school'] = sch_name 
    # person['school'] = input('enter "school" value: ')

# for looping key and value
for key,val in person.items():
    print(key,'is',val)

# sorted looping
for key in sorted(person):
    print( key,'is',person[key])

# looping through the values
print('user info :')
for v in person.values():
    print('\t',v)