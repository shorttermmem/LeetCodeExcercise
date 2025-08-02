#https://leetcode.com/problems/diagonal-traverse-ii/description/
from common_types import *

"""
1424. Diagonal Traverse II
Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

1 2 3
4 5 6
7 8 9

0,0
1,0, 0,1
2,0, 1,1, 0,2
3,0, 2,1, 1,2, 0,3

Example 2:


Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

1,2,3,4,5
6,7
8
9,10,11
12,13,14,15,16

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= sum(nums[i].length) <= 10^5
1 <= nums[i][j] <= 10^5
"""

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        for level in range(levels):
            for c in range(level):
                r = level - c

        return []