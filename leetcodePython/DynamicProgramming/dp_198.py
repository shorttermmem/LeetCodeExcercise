#https://leetcode.com/problems/house-robber/description/

# Exmaple: [2,7,9,3,1] -> 12
#           2,  9,  1 = 12
#             7,  3 = 10
# Example: [1,2,3,1] -> 4

# Constraints:
# 1 <= nums.length <= 100

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]
    
    
#--------------------------------------------------
# Another solution
    def rob2(self, nums: List[int]) -> int:
        
        def _rob(nums)->int:
            
            #top-down approach
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums)
            if len(nums) == 3:
                return max(nums[0]+nums[2], nums[1])
            
            return max(nums[0] + _rob(nums[2:]), nums[1] + _rob(nums[3:]))
        
        return _rob(nums)