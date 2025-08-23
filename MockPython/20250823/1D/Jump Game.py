#https://leetcode.com/problems/jump-game/description/
from common_types import *

"""
You are given an integer array nums. You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Cant: -1
NotSet: 0
Can: 1

arriveStatus[i]

arriveStatus[i-k] = 1
k + nums[i-k] >= i

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        This is not a opt problem, shouldn't be solved with DP
        """

        reachEndStatus = [False] * len(nums)
        reachEndStatus[-1] = True
        for currPos in range(len(nums)-2, -1, -1):
            jumpRange = min(currPos + nums[currPos], len(nums)-1)
            for dest in range(currPos+1, jumpRange+1):
                if reachEndStatus[dest]:
                    reachEndStatus[currPos] = True
                    break
        return reachEndStatus[0]
    
        jumpCount = len(nums) + 1
        reachable = [0] * (jumpCount)
        reachable[0] = 1

        for jc in range(jumpCount):
            jumpIdx = jc - 1
            reachable[jumpIdx] = jc + nums[jumpIdx]
            
        return reachable[-1] == 1


        max_reachable = 0
        for i, n in enumerate(nums):
            max_reachable = max(n + i, max_reachable)
            if max_reachable >= len(nums):
                return True
        return False
        