#https://leetcode.com/problems/coin-change-ii/description/
# combinations to make up amount
# Example: coins = [1, 2, 5], amount = 5
# Output: 4
# Explanation: there are four ways to make up amount 5

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        