#https://leetcode.com/problems/climbing-stairs/

from common_types import *

"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

waysFor(n) = waysFor(n-1) + waysFor(n-2)


"""

class Solution:
    def climbStairs(self, n: int) -> int:

        # n = 3
        #     3-1,          3-2
        #     2-1, 2-2,     1-1 
        #     1-1 
        @lru_cache(None)        
        def waysForSteps(steps) -> int:
            if steps <= 1:
                return 1
            return waysForSteps(steps - 1) + waysForSteps(steps - 2)

        return waysForSteps(n)
    
class SolutionBtUp:
    def climbStairs(self, n: int) -> int:
        ways1StepBefore, ways2StepsBefore = 1, 1
        waysToCurrentStep = 1
        for steps in range(2, n+1):
            waysToCurrentStep = ways1StepBefore + ways2StepsBefore
            ways1StepBefore, ways2StepsBefore = waysToCurrentStep, ways1StepBefore
        return waysToCurrentStep









        