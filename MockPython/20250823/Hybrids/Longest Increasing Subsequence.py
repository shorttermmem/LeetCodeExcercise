#https://leetcode.com/problems/longest-increasing-subsequence/description/
from common_types import *

"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


Input: nums = [7,7,7,7,7,7,7]
Output: 1


for i in range(len(nums)):
    if nums[i] > nums[i-1]:
        maxLengthEndAt[i] = maxLengthEndAt[i-1] + 1

maxLengthEndAt[x]

if nums[x] > nums[x-1]:
    maxLengthEndAt[x] = maxLengthEndAt[x-1] + 1

if nums[x] > nums[x-2]:
    maxLengthEndAt[x] = maxLengthEndAt[x-2] + 1

if nums[x] > nums[x-t]:
    maxLengthEndAt[x] = maxLengthEndAt[x-t] + 1


[......end]........[x]

maxLength = 0


if nums[?] > nums[]

increasing:
# nums[i-1] < nums[i]

LIS(0, len(n)-1) = max(LIS(1, len(n)-1), LIS(0, len(n)-2))


12341

"""
from typing import List

class Solution:
    def _getMaxLengthEndAt(self, index, nums) -> int:
        if index == 0:
            return 1
        maxLength = 1
        for prevEnd in range(index-1, -1, -1):
            if nums[index] > nums[prevEnd]:
                # when a data is increasing, include it in a comparison
                maxLength = max(maxLength, 1 + self._getMaxLengthEndAt(prevEnd, nums))
        return maxLength

    def lengthOfLIS(self, nums: List[int]) -> int:
        maxLength = self._getMaxLengthEndAt(len(nums)-1, nums)
        return maxLength
    

    def lengthOfLIS(self, nums: List[int]) -> int:
                  
        n = len(nums)
        dp = [1] * n
        
        for i in range(n):    
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)    