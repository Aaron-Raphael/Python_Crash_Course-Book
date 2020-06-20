# return is used to return the vwlue after completing the function without printing it inside

def full_name(first , last):
    full = first +' '+ last
    return full

first = input('enter first name : ')
last = input('enter last name : ')

name = full_name(first,last)

print('hi, ' + name)