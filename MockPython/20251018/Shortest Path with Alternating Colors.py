#https://leetcode.com/problems/shortest-path-with-alternating-colors/

from common_types import *

"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. 
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

* redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and

ai -> bi

* blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

uj => vj

Return an array answer of length n, 
where each answer[x] is the 
length of the shortest path from node 0 to node x 
such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

0->1->2


Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 
   
0->1<=2

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n


redPath[src1].append(dst1)

bluePath[src2].append(dst2)

deque[0]

for node in (n):
    deque = [0]
    path = 0
    while deque:
        for dst in deque:
            # when reached node, quit

        # when not reached node
        path += 1

"""


class Solution:
    _RED = 0
    _BLUE = 1
    def _buildPath(self, edges: List[List[int]]):
        path = defaultdict(list)
        for src, dst in edges:
            path[src].append(dst)
        return path

    def _getShortestPath(self, target, levelQue, redPath, bluePath) -> int:
        path = 1
        visited = set()
        while levelQue:
            levelSize = len(levelQue)
            for _ in range(levelSize):
                src, color = levelQue.popleft()
                if (src, color) in visited:
                    return -1
                visited.add((src, color))
                if src == target:
                    return path
                if color == self._RED:
                    for dst in redPath[src]:
                        levelQue.append((dst, self._BLUE))
                else:
                    for dst in bluePath[src]:
                        levelQue.append((dst, self._RED))
            path += 1
        return -1

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redPath = self._buildPath(redEdges)
        bluePath = self._buildPath(blueEdges)
        levelQue = deque()
        answer = [0]
        for target in range(1, n):
            if target in answer:
                continue
            for dst in redEdges[0]:
                levelQue.append((dst, self._BLUE))
            for dst in bluePath[0]:
                levelQue.append((dst, self._RED))
            path = self._getShortestPath(target, levelQue, redPath, bluePath)
            levelQue.clear()
            answer.append(path)
        
        return answer
    

    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # create two seperate tables for each color and map all the connected edges.
        dRed=defaultdict(list)
        dBlue=defaultdict(list)

        for a, b in redEdges:
            dRed[a].append(b)
        
        for a, b in blueEdges:
            dBlue[a].append(b)

        #create list of size n with default value equals -1.

        ans=[-1]*n
        # we will be using heap as ques ask for shortest path.

        heap=[]
        
        #initially we will push 3 elements in heap (count, node, color).
        #default count is zero, default node is 0 and default color is None.
        heapq.heappush(heap, [0,0,None])

        # create a set called visited just to avoid cycle of coming to same node again and again.
        visited=set()
        
        #rest is just a ideal BFS.
        #if color is none, we can all "RED" and "BLUE" path both to the heap otherwise if color is "RED" then add "BLUE" and vice versa.
        while heap:
            cnt, node, color = heapq.heappop(heap)
            if (node, color) not in visited:
                if ans[node]==-1 or ans[node]>cnt:
                    ans[node]=cnt
                visited.add((node, color))
                if color==None:
                    for child in dRed[node]:
                        heapq.heappush(heap, [cnt+1,child,"RED"])
                    for child in dBlue[node]:
                        heapq.heappush(heap, [cnt+1,child,"BLUE"])
                elif color == "BLUE":
                    for child in dRed[node]:
                        heapq.heappush(heap, [cnt+1,child,"RED"])
                elif color == "RED":
                    for child in dBlue[node]:
                        heapq.heappush(heap, [cnt+1,child,"BLUE"])
        return ans