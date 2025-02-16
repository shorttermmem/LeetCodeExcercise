#https://leetcode.com/problems/jump-game-iii/description/
# Example
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        