#https://leetcode.com/problems/jump-game/description/
# is last index reachable
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, nums[i] + i)
        else:
            return True