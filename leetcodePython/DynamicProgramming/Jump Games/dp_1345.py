# #https://leetcode.com/problems/jump-game-iv/description/
# Example 1:
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 
# 0 --> 4 --> 3 --> 9. 
# Note that index 9 is the last index of the array.
from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        pass 
        # DP only solution is O(n^2) and will TLE

    def minJumps_BST(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        # Build value-to-indices map
        value_map = defaultdict(list)
        for i in range(n):
            value_map[arr[i]].append(i)
        
        # BFS
        queue = deque([(0, 0)])  # (index, steps)
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            if idx == n - 1:
                return steps
            
            # Jump to i + 1
            if idx + 1 < n and idx + 1 not in visited:
                queue.append((idx + 1, steps + 1))
                visited.add(idx + 1)
            
            # Jump to i - 1
            if idx - 1 >= 0 and idx - 1 not in visited:
                queue.append((idx - 1, steps + 1))
                visited.add(idx - 1)
            
            # Jump to same-value indices
            for next_idx in value_map[arr[idx]]:
                if next_idx != idx and next_idx not in visited:
                    queue.append((next_idx, steps + 1))
                    visited.add(next_idx)
            
            # Clear processed value to avoid redundancy
            value_map[arr[idx]] = []
        
        return -1  # Unreachable (shouldn’t happen per problem constraints)