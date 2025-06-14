from common_types import *
#https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

"""
Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= nums.length
"""

class Solution:
    # Runtime & Memory tradeoff, two similar ways to implement
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        return 0