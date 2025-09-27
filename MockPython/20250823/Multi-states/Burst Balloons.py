#https://leetcode.com/problems/burst-balloons/description/
from common_types import *

"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[l - 1] * nums[l] * nums[l + 1] coins. If l - 1 or l + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

 

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[l] <= 100


3,1,5,8


maxCoinsAfterBurstBalloons[ballCount] 

"""

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 1Player, 1Action -> 1D
        #         
        nums.insert(0,1)
        nums.append(1)

        def recursive(l, r, memo) -> float:
            if l == r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            
            max_cost = float('-inf')
            
            # the last mid pick within range l, r
            for k in range(l, r):
                curr_cost = nums[l-1] * nums[k] * nums[r] # left - 1, last pick k, right + 1 
                left_cost = recursive(l, k, memo) # left to k - 1 
                right_cost = recursive(k+1, r, memo) # k+1 to right - 1
                max_cost = max(max_cost, curr_cost + left_cost + right_cost)
            
            memo[(l,r)] = max_cost
            return max_cost
        
        memo = {}
        return int(recursive(1, len(nums)-1, memo))

class SolutionBottomUp:
    def maxCoins(self, nums) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for d in range(2, n):
            for left in range(0, n - d):
                right = left + d

                for i in range(left + 1,right):
                    dp[left][right] = max(
                                          dp[left][right], # last collapse max
                                          nums[left] * nums[i] * nums[right]  # curr_cost
                                          + dp[left][i]                       # left_cost
                                          + dp[i][right]                      # right_cost
                                          )
        return dp[0][n - 1]