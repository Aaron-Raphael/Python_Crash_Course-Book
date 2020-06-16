# use input() to prompt anr receive input from user
name = input('enter your name : ').title()
print('Hi,' + name + '!')

# use int to convert input to number or else the numerical value will be store as string
age = int(input('enter your age : '))

print(f"{name} is {age} years old.")