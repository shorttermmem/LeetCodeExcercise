#https://leetcode.com/problems/maximum-alternating-subarray-sum

from common_types import *

"""
A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within an array.

The alternating subarray sum of a subarray that ranges from index i to j (inclusive, 0 <= i <= j < nums.length) is:
nums[i] - nums[i+1] + nums[i+2] - ... +/- nums[j].

Given a 0-indexed integer array nums, return the maximum alternating subarray sum of any subarray of nums.

 

Example 1:

Input: nums = [3,-1,1,2]
Output: 5
Explanation:
The subarray [3,-1,1] has the largest alternating subarray sum.
The alternating subarray sum is 3 - (-1) + 1 = 5.

3

Example 2:

Input: nums = [2,2,2,2,2]
Output: 2
Explanation:
The subarrays [2], [2,2,2], and [2,2,2,2,2] have the largest alternating subarray sum.
The alternating subarray sum of [2] is 2.
The alternating subarray sum of [2,2,2] is 2 - 2 + 2 = 2.
The alternating subarray sum of [2,2,2,2,2] is 2 - 2 + 2 - 2 + 2 = 2.
Example 3:

Input: nums = [1]
Output: 1
Explanation:
There is only one non-empty subarray, which is [1].
The alternating subarray sum is 1.
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105


[-1,1,-1,1] 3

[1,-1,1]

firstSum  2
secondSum -1

firstSum - secondSum = 3


[1,1,-1]

firstSum  2
secondSum -1



added = max(subtracted + curr_num, curr_num)
subtracted = added - curr_num
max(maxNum, added, subtracted)


"""

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> float:
        positiveSum = negativeSum = 0
        maxSum = float('-inf')
        operation = 1
        for rightIndex in range(len(nums)):
            # operation is not +
            positiveSum += operation * nums[rightIndex]
            if currSum < 0:
                # start at next index, as current sum is not contributing
                currSum = 0
            operation *= -1
            maxSum = max(maxSum, currSum)
        return maxSum
    

        
        max_sum = positive = negative = float('-inf')
        for i, num in enumerate(nums):
            positive, negative = max(negative + num, num), positive - num
            max_sum = max(max_sum, positive, negative)
        return max_sum