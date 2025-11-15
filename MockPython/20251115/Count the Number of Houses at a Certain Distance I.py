#https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/description/

from common_types import *

"""
You are given three positive integers n, x, and y.

In a city, there exist houses numbered 1 to n connected by n streets. 
There is a street connecting the house numbered i with the house numbered i + 1 for all 1 <= i <= n - 1. 
An additional street connects the house numbered x with the house numbered y.

For each k, such that 1 <= k <= n, you need to find the number of pairs of houses (house1, house2) such that the minimum number of streets that need to be traveled to reach house2 from house1 is k.


Return a 1-indexed array result of length n where result[k] represents the total number of pairs of houses such that the minimum streets required to reach one house from the other is k.

Note that x and y can be equal.

* the total number of pairs of houses
* minimum streets required to reach one house from the other is k



Example 1:


Input: n = 3, x = 1, y = 3
Output: [6,0,0]
Explanation: Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

result[1] = 6 #

[1, 2, 3]


Extend Example:

Input: n = 3, x = 1, y = 2
Output: [4,2,0]
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

- For the pair (1, 3), need 2.
- For the pair (3, 1), need 2.

Example 2:


Input: n = 5, x = 2, y = 4
Output: [10,8,2,0,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.
Example 3:


Input: n = 4, x = 1, y = 1
Output: [6,4,2,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.
 

Constraints:

2 <= n <= 100
1 <= x, y <= n

(a, b) -> minStreets

n, n+1 -> 1
x, y -> 1


"""
from collections import deque, defaultdict

class Solution:
    def _getMinStreets(self, a, b, streetsFor, positionsFrom) -> int:
        minStreets = 1
        if (a,b) in streetsFor:
            return streetsFor[(a, b)]
        positions = deque([a])
        visited = set()
        while positions:
            positionCount = len(positions)
            for _ in range(positionCount):
                currPos = positions.popleft()
                visited.add(currPos)
                for pos in positionsFrom[a]:
                    if pos in visited:
                        continue
                    if pos == b:
                        streetsFor[(a, b)] = minStreets
                        streetsFor[(b, a)] = minStreets
                        return streetsFor[(a, b)]
                    positions.append(pos)
            minStreets += 1
        # bfs to get min streets
        return 10000

    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        streetsFor = {}
        positionsFrom = defaultdict(list)
        result = [0] * n
        for i in range(1, n):
            positionsFrom[i].append(i+1)
            positionsFrom[i+1].append(i)
            streetsFor[(i, i+1)] = 1
            streetsFor[(i+1, i)] = 1
        
        positionsFrom[x].append(y)
        positionsFrom[y].append(x)
        streetsFor[(x, y)] = 1
        streetsFor[(y, x)] = 1
        # streetsFor[(a, b)] = minStreets, streetsFor[(b, a)] = minStreets
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                k = self._getMinStreets(a, b, streetsFor, positionsFrom)
                result[k-1] += 2

        return result
    


"""
1, 2, 3, 4, 5, 6, 7
   |           |
   -------------

   
   
"""

class Solution2:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        res = [0] * n
        for a in range(1, n+1):
            for b in range(a+1, n+1):
                absPath = abs(b - a)
                bridge1 = abs(a - x) + abs(b - y) + 1
                bridge2 = abs(a - y) + abs(b - x) + 1
                minStreets = min(absPath, bridge1, bridge2)
                res[minStreets-1] += 2
        return res
