#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# sell with cooldown
# Example 1:
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        