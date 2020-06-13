# = is assignment operator
# == is a conditional oooperator

car = 'Audi'
if car.lower() == 'audi':
    print(True)
else:
    print(False)

# != is a inequqlity operator
# < is a less than operator
# > is a greater than operator
# <= is a lesser thann or equal to operator
# >= is a greater than or equal to operrator

age = 19
if age != 0:
    if age <=5:
        print('no ticket')
    elif age<=18:
        print('ticket is $3')
    elif 19<=age<=40:
        print('ticket is $5')
    else:
        print('sorry, not allowed')
else:
    print('enter a valid age')

# boolean gives value True or False