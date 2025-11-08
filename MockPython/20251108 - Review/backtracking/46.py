#https://leetcode.com/problems/permutations

from common_types import *

"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


[1,2,3]

curr = [1] => 1 is taken set define 1 is taken

curr = [2, or 3] => 2 taken or 3 taken

"""

class Solution:

    # P(n k)
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        usedIndex = [False] * len(nums)
        def backtrack(curr):
            if len(curr) == len(nums): # len(curr) == k, solve up to P(n, k)
                result.append(list(curr))
                return
            for index in range(len(nums)):
                if usedIndex[index]:
                    continue
                usedIndex[index] = True
                curr.append(nums[index])
                backtrack(curr)
                usedIndex[index] = False
                curr.pop()

        backtrack([])
        return result