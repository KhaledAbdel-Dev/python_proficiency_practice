def find_multiples(integer, limit):
	
	for i in range(1, limit + 1):
		if i % integer == 0:
			nums.append(i) # append function, adds values to an array
				       # loop allows it to do so iteratively
