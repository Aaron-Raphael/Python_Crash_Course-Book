bikes = ['honda' , 'yamaha' , 'suzuki']
print(bikes)

# item changed by indexing
bikes[0] = 'ducati'
print(bikes)

# adding element to end of list by append()
bikes.append('honda')
print(bikes)

# items inserted by indexing insert
bikes.insert(3,'ktm')
print(bikes)

# items removed by del
del bikes[0]
print(bikes)

# items removed by pop
bikes.pop()
print(bikes)

# remove by indexing pop
bikes.pop(-1)
print(bikes)

# removing by value
bikes.remove('suzuki')
print(bikes)