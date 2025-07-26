#https://leetcode.com/problems/longest-arithmetic-subsequence/description/
from common_types import *

"""
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].
 

Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500


9 4 7 2 10 5 3 # lower triangular iteration

9 -----------                   

9 4          |              lengthAtIndexWithDiff[1][5] = 2

9 4 7        |              lengthAtIndexWithDiff[2][2] = 2      lengthAtIndexWithDiff[2][-3] = 2

9 4 7 5      |              lengthAtIndexWithDiff[3][4] = 2      lengthAtIndexWithDiff[3][-1] = 2   lengthAtIndexWithDiff[3][2] = 3 # lengthAtIndexWithDiff[2][2]   or [3][7] or [3][5]

9...         |

9 4 7 2 10 5 3

# 1 array, find all combinations of substractions

lengthAtIndexWithDiff




"""
from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        lengthAtIndexWithDiff = [defaultdict(int) for _ in range(len(nums))] #cache max common `diffs` subseq length till index
        maxLength = 0
        # lower triangular iterating nums with endIndex, enumerate all pairwise diff within current anchoring
        for endIndex in range(1, len(nums)):
            for i in range(endIndex):
                currDiff = nums[i] - nums[endIndex] # find a pair diff
                
                lengthAtIndexWithDiff[endIndex][currDiff] = 1 + lengthAtIndexWithDiff[i][currDiff] # accumulate existing subseq with the same length
                maxLength = max(maxLength, lengthAtIndexWithDiff[endIndex][currDiff])

        return maxLength + 1


        """
        subSeqLengthAt = [[0] * (len(nums2) + 1) for _ in range(len(nums1)+1)]
        # two arrays
        # full 2D iterations
        for i1 in range(1, len(nums)+1):
            for i2 in range(i1):
                skipI1 = subSeqLengthAt[i1-1][i2]
                skipI2 = subSeqLengthAt[i1][i2-1]
                takeBoth = 0                
                if nums1[i1-1] == nums2[i2-1]:
                    takeBoth = 1 + subSeqLengthAt[i1-1][i2-1]
                subSeqLengthAt[i1][i2] = max(skipI1, skipI2, takeBoth)

        return subSeqLengthAt[-1][-1]
        """

        

