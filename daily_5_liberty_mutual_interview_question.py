# this is was my own iteration, first time while whiteboarding

def most_freq_city(cities: List[str] -> str)

	size = len(cities)
	
	if size == 0:
		return 'list empty'
	elif size == 1:
		return cities
	elif size > 1:
		cities.sort()
		return cities[0]
