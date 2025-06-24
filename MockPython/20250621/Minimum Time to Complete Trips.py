#https://leetcode.com/problems/minimum-time-to-complete-trips/description/
"""
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. 
Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. 
Return the minimum time required for all buses to complete at least totalTrips trips.

Example 1:

Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.



Example 2:

Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.
 

Constraints:

1 <= time.length <= 10^5
1 <= time[i], totalTrips <= 10^7

3k
>= 10^6 O(logn) or O(1)
< 10^6  O(n) or O(nlogn)

bus take less time will finish more trip

time = [1,2,3], totalTrips = 5

iterate through time

iterate from small time to big, and calculate trips

totalTime / time[i]
-------
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
-------

O(logn) O(n) -> binaryserach 

"""

from common_types import *

class Solution:
    def _isTimeAchievable(self, sortedBusTripTime, guessTime, totalTrips) -> bool:
        # guessTime = 1, [1,2,3], 5
        currentTrips = 0
        for busTripTime in sortedBusTripTime:
            currentTrips += guessTime // busTripTime      # currentTrips = 1
            if currentTrips >= totalTrips:
                return True
        return currentTrips >= totalTrips       # 1 < 5

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        sortedBusTripTime = sorted(time)                  # [1, 2, 3], 5
        
        minTime = 1                                     
        maxTime = totalTrips * sortedBusTripTime[0]       # 5/1 = maxTime = 5
        answer = 1
        
        while minTime <= maxTime:
            guessTime = (minTime + maxTime) // 2          # guessTime = 1
            if self._isTimeAchievable(sortedBusTripTime, guessTime, totalTrips):
                answer = guessTime
                maxTime = guessTime -1                    #maxTime = 3-1 = 2
            else:
                minTime = guessTime + 1                   #minTime = 2
        return answer
    
##########
         while minTime < maxTime:
            guessTime = (minTime + maxTime) // 2
            if self._isTimeAchievable(sortedBusTripTime, guessTime, totalTrips):
                maxTime = guessTime - 1
            else:
                minTime = guessTime + 1

        return minTime




