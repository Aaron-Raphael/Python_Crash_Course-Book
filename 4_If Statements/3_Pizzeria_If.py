# in checks if item is in list

topping_available = ['mushrooms', 'olives', 'green peppers',
                     'pepperoni', 'pineapple', 'extra cheese']

topping_req = ['mushrooms', 'french fries', 'extra cheese']

for req in topping_req:
    if req in topping_available:
        print(req,'is added')
    else:
        print(req,'not available')

print('your pizza is finished')