#https://leetcode.com/problems/climbing-stairs/
from common_types import *

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

1 step, 2 step option

for each k within n steps

waysToReachStep[k] = waysToReachStep[k-1] + waysToReachStep[k-2]
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        # Mem opt

        ways1StepAway, ways2StepsAway = 1, 1
        for i in range(2, n+1):
            currentWays = ways1StepAway + ways2StepsAway
            ways1StepAway, ways2StepsAway = currentWays, ways1StepAway
        return ways1StepAway        

        # Brute force
        waysToReachStep = [1] * (n + 1) # nth value is the number of ways to climb there, hence size n+1 
                                        # base value is at least 1 way to climb
        for i in range(2, n+1):
            # n = 2 => 1, 1 => 2
            # n = 3 => 2, 1 => 3
           waysToReachStep[i] = waysToReachStep[i-1] + waysToReachStep[i-2]
        return waysToReachStep[-1]
    
    
