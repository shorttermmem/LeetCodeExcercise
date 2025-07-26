#https://leetcode.com/problems/uncrossed-lines/description/
from common_types import *

"""
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) 

on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.


1   4   2
|     \
1   2   4

X X X X
 / \ X /
X X X X

1 1 1
| | |
1 1 1


Example 1:
Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.

To build a cross line:
1. same element in array1 and array2
2. 





Example 2:







Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2
 

Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000


5 1 3

1 3 2 5
      1 3 2 5
    0 1 2 3 4
  0 0 0 0 0 0
5 1 0 0 0 0 1
1 2 0 1 0 0 1
3 3 0 1 2 2 2
"""

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        subSeqLengthAt = [[0] * (len(nums2) + 1) for _ in range(len(nums1)+1)]
        for i1 in range(1, len(nums1)+1):
            for i2 in range(1, len(nums2)+1):
                skipI1 = subSeqLengthAt[i1-1][i2]
                skipI2 = subSeqLengthAt[i1][i2-1]
                takeBoth = 0                
                if nums1[i1-1] == nums2[i2-1]:
                    takeBoth = 1 + subSeqLengthAt[i1-1][i2-1]
                subSeqLengthAt[i1][i2] = max(skipI1, skipI2, takeBoth)

        return subSeqLengthAt[-1][-1]











