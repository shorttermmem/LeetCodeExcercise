#https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

from typing import List
from bisect import bisect_right

# priority queue + dp + binary search

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # sort by endTime
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x:x[1])

        dp = [[0,0]] # [end_time, max_profit]

        for start, end, profit in jobs:

            # Find the latest job that doesn't overlap with the current job
            # Using binary search on the DP array
            i = bisect_right(dp, [start, float('inf')]) - 1

            # take curr profit
            max_profit = dp[i][1] + profit

            # If including the current job yields a higher profit, add it to the DP array
            if max_profit > dp[-1][1]:
                dp.append([end, max_profit])


        return dp[-1][-1]