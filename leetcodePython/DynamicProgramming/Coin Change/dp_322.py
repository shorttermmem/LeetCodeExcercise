#https://leetcode.com/problems/coin-change/description/
# min coins to make up amount
# Example: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        