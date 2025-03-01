#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
# a fixed fee per transaction
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int: