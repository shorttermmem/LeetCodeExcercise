#https://leetcode.com/problems/car-pooling/description/

# Example 1:      [num, from, to]
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# Example 2:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
 
class Solution:
    def carPooling_heap(self, trips: List[List[int]], capacity: int) -> bool:
             
        # sort by end
        trips.sort(key=lambda x:x[1])
        res = 0
        
        # greedy: restore seats from prev stops
        heap = [] # (to, num)

        for num_, from_, to_ in trips:
            # greedy: restore seats from prev stops
            while heap and heap[0][0] <= from_:
                capacity += heappop(heap)[1]
                
            capacity -= num_
    
            if capacity < 0:
                return False

            # cache prev destination and seats
            heappush(heap, (to_, num_))
        return True
    
    def carPooling_sweepline(self, trips: List[List[int]], capacity: int) -> bool:
        # sweep line algo
        # from, take seats
        # to, return seats

        # if from and to are the same, sorted will use +- num
        # we should allow restore seats before taking.
        # hence [fr, num] should be positive
        for pos, seats in sorted([e for num, fr, to in trips for e in [[fr, num], [to, -num]]]):
            capacity -= seats
            if capacity < 0:
                return False
        return True
         