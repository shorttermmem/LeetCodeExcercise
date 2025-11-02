#https://leetcode.com/problems/redundant-connection/description/

from common_types import *

"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. 
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

1-2
|/
3
uf = UF()
for pt1, pt2 in edges:
    uf.add(pt1), uf.add(pt2)
    if uf.find(pt1) == uf.find(pt2):
        return [pt1, pt2]
    uf.union(pt1, pt2)
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

class UF:
    def __init__(self):
        self._rank = Counter()
        self._parent = defaultdict()
        self._count = 0
        return

    def add(self, data) -> None:
        if data not in self._parent:
            self._parent[data] = data
            self._rank[data] = 0
            self._count += 1
       
    def valid(self, data) -> bool:
        return self._parent.get(data) is not None

    def find(self, data):
        if self._parent.get(data)
       
    def union(self, data1, data2) -> None:
        root1 = self.find(data1)
        root2 = self.find(data2)
        if root1 == root2:
            return
        rank1, rank2 = self._rank[root1], self._rank[root2]
        if rank1 > rank2:
            self._parent[root2] = root1
        elif rank1 < rank2:
            self._parent[root1] = root2
        else:
            self._parent[root2] = root1
            self._rank[root1] += 1

        self._count -= 1

    def __len__(self):
        return self._count
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF()
        for pt1, pt2 in edges:
            uf.add(pt1), uf.add(pt2)
            if uf.find(pt1) == uf.find(pt2):
                return [pt1, pt2]
            uf.union(pt1, pt2)
        return []