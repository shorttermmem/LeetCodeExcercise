from common_types import *
#https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

"""
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= nums.length


[1,2,2,3,3,1,3] k=2 => 6

1, Contiguous subarray not subsequence

[1,2,3,2,3] k = 1
"""

class Solution:
    # Runtime & Memory tradeoff, two similar ways to implement
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        freqOf = Counter()
        for right in range(len(nums)):
            newNum = nums[right]            # [1, 2, 3, 2, 3]
            freqOf[newNum] += 1             #        l  r
            
            #TODO here cant be if, we need to know when we can.
            while freqOf[newNum] > k:
                oldNum = nums[left]         # [2]
                freqOf[oldNum] -= 1         #  freq[2] = 1
                if not freqOf[oldNum]:      
                    del freqOf[oldNum]
                left += 1                   # l = 1.      3-1+1 = 3
                
        return right - left + 1
    
    def maxSubarrayLength_opt(self, nums: List[int], k: int) -> int:
        left = 0
        indexesOf = defaultdict(deque)
        maxLength = 0
        for right in range(len(nums)):
            newNum = nums[right]            # [1, 2, 3, 2, 3]
            indexesOf[newNum].append(right)
            if len(indexesOf[newNum]) > k:
                left = max(left, indexesOf[newNum].popleft() + 1)
            maxLength = max(maxLength, right - left + 1)
        return maxLength
    




    