#https://leetcode.com/problems/find-k-closest-elements/description/
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# Output: [1,1,2,3]

#------------ Why bisect_left instead of bisect_right --------------------------------------------
# We need to find k elements closest to x, which means:
# The selected k elements should have the smallest absolute difference with x.
# If there is a tie (two elements are equally distant), 
# we must choose the smaller elements (which means choosing a subarray that is more left-leaning).
#-------------------------------------------------------------------------------------------------

from typing import List
from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # takes an index mid and compares the distances of arr[mid] and arr[mid + k] from x.
        # If arr[mid] is farther than arr[mid + k] (or equally distant but larger), 
        # it returns True, meaning the left boundary should move right.
        compare = lambda mid: arr[mid] - x >= x - arr[mid + k]

        # this performs binary search on possible mid values [0, len(arr) - k - 1].
        # It finds the smallest mid where compare(mid) is True,
        # determining the leftmost position of the k closest elements.
        left = bisect_left(range(len(arr) - k), True, key=compare)
        return arr[left:left + k]
        

        def slow_solution():
            # for max heap
            heap = []

            for v in arr:
                dist = abs(v - x)

                if len(heap) < k:
                    heapq.heappush(heap, (-dist, v))
                else:
                    if heap[0][0] < -dist:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-dist, v))
                        
            return sorted([v for _, v in heap])
            