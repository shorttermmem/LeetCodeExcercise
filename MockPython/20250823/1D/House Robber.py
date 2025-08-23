#https://leetcode.com/problems/house-robber/description/
from common_types import *

"""
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


totalGainAt[i] = nums[i] + totalGainAt[i-2]

totalGainAt[i] = totalGainAt[i-1]

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        totalGainWith = [0] * (len(nums) + 1)
        totalGainWith[1] = nums[0]
        # 1, 2
        #totalGainAt[2] = nums[2] + totalGainAt[2-2]
        #totalGainAt[2] = totalGainAt[1]
        for houseCount in range(2, len(nums)+1): # 
            houseIndex = houseCount - 1 # curr 
            totalGainWith[houseCount] = max(nums[houseIndex] + totalGainWith[houseCount-2], totalGainWith[houseCount-1])
        return totalGainWith[len(nums)]
    


        # NUMBER of step to get solution
        #                                   Number of houses looked at
        # look up cache of prev solutions