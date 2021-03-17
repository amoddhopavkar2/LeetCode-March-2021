# Tuesday, 16th March 2021
# Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buying, selling = 0, -prices[0]

        for price in prices:
            buying = max(buying, selling + price - fee)
            selling = max(selling, buying - price)
        
        return buying