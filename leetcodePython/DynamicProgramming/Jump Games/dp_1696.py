#https://leetcode.com/problems/jump-game-vi/description/
# max score in k steps or less
# Example 1:
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# Explanation: You can choose your jumps forming the subsequence [1,4,3] of length 3, with the sum of the elements equal to 7.

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # dp[i] = max score at index i
        # dp[i] = max(dp[i-k:i]) + nums[i]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            #
            dp[i] = max(dp[max(0, i-k):i]) + nums[i]
            
        return dp[-1]