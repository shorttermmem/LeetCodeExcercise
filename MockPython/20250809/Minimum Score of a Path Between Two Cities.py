#https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
from common_types import *

"""
You are given a positive integer n representing n cities numbered from 1 to n. 
You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. 
The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
 

Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
 

Constraints:

2 <= n <= 10^5
1 <= roads.length <= 10^5
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 10^4
There are no repeated edges.
There is at least one path between 1 and n.

BFS, DFS, UF


"""

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        visited = set()

        currentCitys = deque([1])
        path = defaultdict(list)
        
        pathDistance = {}
        for src, dst, distance in roads:
            path[src].append(dst)
            pathDistance[(src, dst)] = distance
            path[dst].append(src)
            pathDistance[(dst, src)] = distance

        minDistance = float("inf")
        while currentCitys:
            cityCount = len(currentCitys)
            for i in range(cityCount):
                city = currentCitys.popleft()
                for nextCity in path[city]:
                    if (city, nextCity) in visited:
                        continue
                    visited.add((city, nextCity))
                    visited.add((nextCity, city))
                    currentCitys.append(nextCity)
                    minDistance = min(minDistance, pathDistance[(city, nextCity)])
        return minDistance