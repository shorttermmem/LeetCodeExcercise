# https://leetcode.com/problems/gas-station/description/
from types import List

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if solution does not exist
        if sum(gas) < sum(cost):
            return -1

        # find start position
        deficit = 0
        start = 0

        for i in range(len(gas)):
            # What does `gas[i] - cost[i]` represent, and why track it?
            deficit += gas[i] - cost[i]

            # If you run out of gas starting at station A, what does it imply about A and the next station?
            if deficit < 0:
                # Why does resetting the start after a negative tank work?
                start = i + 1
                deficit = 0

        # How do you prove that if a solution exists, your algorithm finds it?
        return start
    

#-------------------------------------------------------------------------------
#Crucial observation: If k fails at m, the valid starting point must be after m. Why?
# If we started before m (e.g., at k), we’d hit the same deficit at m (since the circular route includes that segment).
# The total sum being non-negative (total >= 0) implies there’s a surplus later in the loop (after m) that offsets this deficit.
# Thus, a valid start must begin after the deficit, where the tank can stay non-negative by “front-loading” the surplus.
