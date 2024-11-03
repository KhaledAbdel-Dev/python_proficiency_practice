# this is the corrected version with my errors fixed

from typing import List # library for lists
from collections import Counter # library for the counter function

def most_freq_city(cities: List[str]) -> str: # syntax error with the parentheses

	size = len(cities)
	
	if size == 0:
		return 'list empty'
	elif size == 1:
		return cities[0] # returns the value as a string as opposed to a single element list
	elif size > 1:
		# use collections.Counter() to count iterations of each element in a list
		city_counter = Counter(cities)
		# most.common() is a method provided by the Counter class
		# it returns a tuple, the element and its frequency
		most_common_city, _  = city_counter.most_common(1)[0] # here we're unpacking the tuple and returning the element individually
		return most_common_city 

# this function now works recursively btw
