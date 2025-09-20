#https://leetcode.com/problems/house-robber/description/
from common_types import *

"""
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

maxGainWithHouses = [0] * (len(nums) + 1)

Options:
* rob current house => prev house not rob
* don't rob current house => take prev max gain

maxGainWithHouses[x] = max(nums[x] + maxGainWithHouses[x - 2], maxGainWithHouses[x-1])
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxGainAt = [0] * len(nums)
        maxGainAt[0] = nums[0]
        if len(nums) < 2:
            return maxGainAt[0]
        maxGainAt[1] = max(nums[0], nums[1]) 
        for houseIndex in range(2, len(maxGainAt)):                
            maxGainAt[houseIndex] = max(nums[houseIndex] + maxGainAt[houseIndex -2], maxGainAt[houseIndex -1])
        return maxGainAt[len(nums)-1]

"""
robStartAt[index] = max(nums[index]+robStartAt[index+2], robStartAt[index+1])
"""
from functools import *
from typing import List

class SolutionTopDown:
    def rob(self, nums: List[int]) -> int:
        @cache
        def _robGainStartAt(index) -> int:
            if index >= len(nums):
                return 0
            return max(nums[index] + _robGainStartAt(index+2), _robGainStartAt(index+1))
        return _robGainStartAt(0)
    














from functools import cache
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        @cache
        def rob_from_index(index: int) -> int:
            # Base cases
            if index >= len(nums):
                return 0
            if index == len(nums) - 1:
                return nums[index]
            # Recursive case: compute for smaller subproblems first
            return max(
                nums[index] + rob_from_index(index + 2),  # Rob current house
                rob_from_index(index + 1)  # Skip current house
            )

        # Start from the smallest index to emulate bottom-up
        # Compute all subproblems up to index 0
        for i in range(len(nums) - 1, -1, -1):
            rob_from_index(i)
        
        return rob_from_index(0)    