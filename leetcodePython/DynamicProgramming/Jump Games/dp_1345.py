# #https://leetcode.com/problems/jump-game-iv/description/
# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 
# 0 --> 4 --> 3 --> 9. 
# Note that index 9 is the last index of the array.

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        