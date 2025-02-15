#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

# States: profit at ith
# Actions: buy or sell