#https://leetcode.com/problems/jump-game-vii/description/
# binary string limits landing positions.
# Example 1:
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation: In the first step, move from index 0 to index 3.
# In the second step, move from index 3 to index 5.

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
    
