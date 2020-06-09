# using apostrophe inside a singlequote string produces error
# use apostophe inside a doublequote strong to avoid error
  
message_1 = "Python's strength is its diverse comunity."
print(message_1)


# using doublequotes inside a doublequote string produces error
# use doubleqoute inside asingle quote string to avoid error
message_2 = 'He said, "Hello".'
print(message_2)

# formatted string to avoid syntax  error
name =  'Aaron'
age = 19
message_3 = f"{name}'s age is {age}"
print(message_3)