# tuples are immutable lists
# represented by()

dimention = (10, 5, 5)
print(dimention)

# looping through tuple
for i in dimention:
    print(i)

# slicing tuple
xy = dimention[:2]
print(xy)

# converting tuple to list
list_conv = list(dimention)
print(list_conv)

# immutable but can alter values
dimention = (5,)
print(dimention)