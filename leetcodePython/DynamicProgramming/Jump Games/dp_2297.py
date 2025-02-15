#https://leetcode.com/problems/jump-game-viii/description/
# different cost to jump
# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.

class Solution:
    def min_cost(self, nums: List[int], costs: List[int]) -> int: