cars = ['bmw' , 'audi' , 'mercedes']
print(cars)

# list slicing using[:]
cars_1 = cars[:]

# permanent sorting
# alphabetical sort by sort()
cars_1.sort()
print(cars_1)

#reverse alphabetical 
cars_1.sort(reverse=True)
print(cars_1)

# temporary sorting
print(sorted(cars))

# reversed list
cars.reverse()
print(cars)

# length of list
print(len(cars))

# position using index starting from 0
print(cars.index('audi'))