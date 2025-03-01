#https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/
#
# [[LINE SWEEP ALGORITHM]]
#
# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.

from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:

        from bisect import bisect_left, bisect_right

        # starts are sorted in ascending order
        # ends are sorted in ascending order
        starts, ends = map(sorted, zip(*flowers))
        
        # bisect_right(starts, time): Counting how many intervals have started by the given time.
        # bisect_left(ends, time): Counting how many intervals have ended before the given time.
        return [bisect_right(starts, person) - bisect_left(ends, person) for person in people]





        def fullBloomFlowers_heap():


            # DOESNT WORK
            # TODO
            import heapq

            observation_times = sorted(people)
            flowers.sort() # sort by start time

            curr_blossom = {}
            ends_heap = []

            idx = 0
            for time in observation_times:

                while idx < len(flowers) and flowers[idx][0] <= time:
                    start, end = flowers[idx]
                    heapq.heappush(ends_heap, end)
                    curr_blossom[end] = curr_blossom.get(end, 0) + 1
                    idx += 1

                while ends_heap and ends_heap[0] <= time:
                    end = heapq.heappop(ends_heap)
                    curr_blossom[end] -= 1

                curr_blossom[time] = curr_blossom.get(time, 0) + 1

            res = [curr_blossom[time] for time in observation_times]
            return res 