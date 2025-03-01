#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
# at most k transactions

# Example 1:
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        