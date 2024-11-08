# LC 771 - EASY

class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:

		set_of_jewels = set(jewels)

		counter = 0

		for stone in stones:
			if stone in set_of_jewels:
				counter += 1

		return counter

	# OH GAWD i love this solution, set func go brrrrrr
