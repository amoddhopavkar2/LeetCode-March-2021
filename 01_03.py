# Monday, 1st March 2021
# Distribute Candies

class Solution:
	def distributeCandies(self, candyType: List[int]) -> int:
		types = len(set(candyType))
		max_candies = len(candyType) // 2
		
		return min(types, max_candies)
		
