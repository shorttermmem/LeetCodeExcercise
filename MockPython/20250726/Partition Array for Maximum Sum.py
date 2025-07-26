#https://leetcode.com/problems/partition-array-for-maximum-sum/description/
from common_types import *

"""
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. 
After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,    9,            2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]

[1,15,7]
[]

largestSumAtIndex[i]


Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83

[1,4,1,5]. [5,5,5,5]    20
[7].       [7]          7
[3,6,1,9]  [9,9,9,9]    36
[9,3].     [9,9]        18





Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length


[1,4,1,5,7,3,6,1,9,9,3]   k = 4

[1,4,1,5,  7,3,6,    1,9,9,3] 
"""

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        for right in range(len(arr)):
            start = max(0, right-k)
            for left in range(start, right):
                currMaxArea = width * currMaxHeight
                maxAreaUntil[right] = max(maxAreaUntil[right], currMaxArea+maxAreaUntil[left-1])
        return maxAreaUntil[-1]
                # arr[left:right+1]