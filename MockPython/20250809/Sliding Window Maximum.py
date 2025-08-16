#https://leetcode.com/problems/sliding-window-maximum/description/
from common_types import *

"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

memory O(k)
runtime O(n)

[1, 3, -1] 2
    3
    1

[0]
[1, 2]

[1, 3]

decreaseQueue

k = 3

9,9,9,1

[9,9,9] + 1, - 9

"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decreaseDataIndex = deque()
        answer = []
        for i in range(k):
            while decreaseDataIndex and nums[decreaseDataIndex[-1]] < nums[i]:
                decreaseDataIndex.pop()
            decreaseDataIndex.append(nums[i])
        
        answer.append(nums[decreaseDataIndex[0]])

        for right in range(k, len(nums)):
            left = right - k
            while decreaseDataIndex and nums[decreaseDataIndex[-1]] <= nums[right]:
                decreaseDataIndex.pop()
            decreaseDataIndex.append(right)
            if decreaseDataIndex and decreaseDataIndex[0] <= left:
                decreaseDataIndex.popleft()
            answer.append(nums[decreaseDataIndex[0]])
        return answer