# learned alot
def nb_year(p0, percent, aug, p):

	current = p0
	years_needed = 0

	while current < p:
		growth = int(current * (percent / 100) + aug)
		current += growth
		years_needed += 1

	return years_needed
