# using as to call function by alias

from pizza import make_pizza as mp 

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#  modules can alsobe imported as alias

import pizza as joey

joey.make_pizza(16, 'pepperoni')
joey.make_pizza(12, 'ham', 'bbq chicken', 'extra cheese')