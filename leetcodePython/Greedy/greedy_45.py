
#https://leetcode.com/problems/jump-game-ii/description/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        curr_reach = 0 #The boundary of your current “ladder rung.”
        next_reach = 0 #The potential boundary of the next rung, updated as you explore.
        jumps = 0

        for i in range(len(nums) - 1):
            next_reach = max(next_reach, nums[i] + i)
            # The key is to jump only when you’ve exhausted your current reach and move to the next maximum reach, not every time you extend it.
            if i == curr_reach:
                jumps+=1
                curr_reach = next_reach
        return jumps if curr_reach >= len(nums) - 1 else -1



        # --- wrong solution
        reachable = 0
        max_reachable = 0
        res = 0
        for i in range(len(nums) - 1):
            reachable = nums[i] + i
            #You’re incrementing res every time a new index pushes max_reachable further, but this counts jumps for every extension, not the minimum needed.
            # you’re not grouping how far you can go in one jump before deciding to take the next.
            if reachable > max_reachable:
                res +=1
                max_reachable = reachable
        return res if max_reachable >= len(nums) - 1 else -1