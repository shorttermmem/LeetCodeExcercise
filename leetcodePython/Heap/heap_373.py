#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Bruteforce: O(n^2) time complexity
# Optimization: O(nlogn) time complexity

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []

        n1, n2 = len(nums1), len(nums2)

        for i in range(min(k, n1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        res = []

        while heap and len(res) < k:
            curr_sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])

            if j + 1 < n2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
