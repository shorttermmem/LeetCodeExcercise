#https://leetcode.com/problems/choose-k-elements-with-maximum-sum/description/

from common_types import *

"""
You are given two integer arrays, nums1 and nums2, both of length n, along with a positive integer k.

For each index i from 0 to n - 1, perform the following:

* Find all indices j where nums1[j] is less than nums1[i].
* Choose at most k values of nums2[j] at these indices to maximize the total sum.
Return an array answer of size n, where answer[i] represents the result for the corresponding index i.

for each i:
* find all j: nums1[j] < nums1[i]

within j:
k of nums2[j]
max(sum(nums2[ k of j]))

Example 1:

Input: nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2

Output: [80,30,0,80,50]

Explanation:

For i = 0: Select the 2 largest values from nums2 at indices [1, 2, 4] where nums1[j] < nums1[0], resulting in 50 + 30 = 80.
For i = 1: Select the 2 largest values from nums2 at index [2] where nums1[j] < nums1[1], resulting in 30.
For i = 2: No indices satisfy nums1[j] < nums1[2], resulting in 0.
For i = 3: Select the 2 largest values from nums2 at indices [0, 1, 2, 4] where nums1[j] < nums1[3], resulting in 50 + 30 = 80.
For i = 4: Select the 2 largest values from nums2 at indices [1, 2] where nums1[j] < nums1[4], resulting in 30 + 20 = 50.


[4,2,1,5,3]    [10,20,30,40,50]
2,1,3 < 4
[1,2,4]

two data smaller than 3
      2
1, 2, 3, 4, 5
2, 1, 4, 0, 3


[50, 20, 30] => [20, 30, 50]
k = 2 => 30 + 50 = 80
O(n^2*logn)
O(n*m*log(m) + n*n))

* n indices
* nlogn sorting


sorting nums2 first, but build index relationship
nums1 => index
index => num2Value => sortedNum2Index


Example 2:

Input: nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1

Output: [0,0,0,0]

Explanation:

Since all elements in nums1 are equal, no indices satisfy the condition nums1[j] < nums1[i] for any i, resulting in 0 for all positions.
"""

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        answer = []
        for i, num in enumerate(nums1):
            indicesFor_i = []
            for i1 in range(len(nums1)):
                if nums1[i1] < num:
                    indicesFor_i.append(i1)
            filteredNums2 = [nums2[j] for j in indicesFor_i]
            filteredNums2.sort()
            sum_i = 0
            k2 = min(len(filteredNums2), k)
            for t in range(k2):
                sum_i += filteredNums2[len(filteredNums2)-1-t]
            answer.append(sum_i)
        return answer
    













    