#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# at most two transactions

# Example 1:
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Total profit is 3 + 3 = 6.

class Solution:
    def maxProfit(self, prices: List[int]) -> int: