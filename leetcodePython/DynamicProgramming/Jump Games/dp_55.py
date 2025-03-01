from typing import List


class SolutionReverseDP:
    def canJump(self, nums: List[int]) -> bool:
        BOUNDARY = len(nums) - 1
        SUCCEED, FAILED, UNKNOWN = 1, 0, -1
        pos_finish_status = [UNKNOWN] * (len(nums) - 1)
        pos_finish_status.append(SUCCEED)

        for i in range(len(nums)-2, -1, -1):
            furthest = min(i + nums[i], BOUNDARY)
            for j in range(i+1, furthest + 1):
                if pos_finish_status[j] == SUCCEED:
                    pos_finish_status[i] = SUCCEED
                    break
        return pos_finish_status[0] == SUCCEED


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reverse_pos = len(nums) - 1
        for reverse_i in range(len(nums)-1, -1, -1):
            if reverse_i + nums[reverse_i] >= reverse_pos:
                reverse_pos = reverse_i
        return reverse_pos == 0

#https://leetcode.com/problems/jump-game/description/
# is last index reachable
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true

class Solution:
    # top-down approach with memoization
    def canJump(self, nums: List[int]) -> bool:
            
        def _recur(start, memo) -> bool:
            if len(nums) <= start + 1:
                return True
            
            # Memo to store the result of the current index
            # was using (start, i) as key, but it's not necessary
            if start in memo:  
                return memo[start]
            
            max_step = nums[start]
            
            for i in range(1, max_step+1):
                
                if _recur(start+i, memo):
                    memo[start] = True
                    return True
            memo[start] = False    
                
            return False
        return _recur(0, {})
    
    # bottom-up approach with tabulation    
    def canJump2(self, nums: List[int]) -> bool:
        # dp[i] = True if it's possible to reach the end from i
        # dp[i] = any(dp[i+1:i+1+nums[i]])
        
        if (0): # back to front
            dp = [False] * len(nums)
            dp[-1] = True
            
            for i in range(len(nums)-2, -1, -1):
                for j in range(1, nums[i]+1):
                    if dp[i+j]:
                        dp[i] = True
                        break
            return dp[0]
    
        if (1): # front to back
            dp = [False] * len(nums)
            dp[0] = True
            for i in range(1, len(nums)):
                # check if any of the previous index can reach the current index
                for j in range(i):
                    if dp[j] and j + nums[j] >= i:
                        dp[i] = True
                        break
            return dp[-1]
    
    
        
        