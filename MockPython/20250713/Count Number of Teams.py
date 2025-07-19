#https://leetcode.com/problems/count-number-of-teams/description/
from common_types import *

"""
There are n soldiers standing in a line. Each soldier is assigned a "unique" rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: 
1. (rating[i] < rating[j] < rating[k]) 
2. or (rating[i] > rating[j] > rating[k]) 
3. where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3

Explanation: We can form three teams given the conditions. 
(2,3,4), 
(5,4,1), 
(5,3,1). 


[2,5,3,4,1]

2, 5, 3, 4
   5, xxxxx
      3. xxxx
                    0, 1, 2
numOptionsAtIndex[i][]

* for each soldier
  * how many soldier have higher
  * lower rating at the right index of it.


Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:


Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique.

"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        totalCount = 0
        for mid in range(1, len(rating)-1):
            leftSmallerCount, leftBiggerCount = 0, 0
            for left in range(mid):
                if rating[left] < rating[mid]:
                    leftSmallerCount += 1
                else:
                    leftBiggerCount += 1
            rightSmallerCount, rightBiggerCount = 0, 0
            for right in range(mid+1, len(rating)):
                if rating[right] < rating[mid]:
                    rightSmallerCount += 1
                else:
                    rightBiggerCount += 1
            increaseCount = leftSmallerCount * rightBiggerCount
            decreaseCount = leftBiggerCount * rightSmallerCount
            totalCount += increaseCount + decreaseCount
        return totalCount