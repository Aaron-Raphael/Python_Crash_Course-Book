def greet(name):
    print('hello',name)     # the name inside the function is parameter

name = input('enter your name: ')

greet(name)     # name passed to the function is argument

# positional arguments are refered by position of passing

# default values ure set to produce outpput if value is defaullt and not passed
# non default argument are passed before default arg
def pet(owner,p_name,pet_type = 'parrot'):
    print(owner + ' ownes a ' + pet_type + ' named ' + p_name)

o_n = input('enter name : ')
p_t = input('enter pet kind : ')
p_n = input('enter pet name : ')

pet(o_n , p_n , p_t)     # here by position arguments passes to parameter

# key word arguments pass arguments by keyword 
# in key word arguments position dont mater
pet(p_name=p_n , owner=o_n , pet_type= p_t)

# function by defalut value
pet(owner=o_n , p_name=p_n)