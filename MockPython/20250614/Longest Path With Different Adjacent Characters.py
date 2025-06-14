from common_types import *
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

"""
You are given a tree (i.e. a connected, undirected graph that has no cycles) 
rooted at node 0 consisting of n nodes numbered from 0 to n - 1.
The tree is represented by a 0-indexed array parent of size n,
where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent 
nodes on the path have the same character assigned to them.

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.

Input: parent = [-1,0,0,1,1,2], s = "abacbe"


"""

class Solution:
    def _maxNonAdjacentDepth(self, rootIndex, childOf, s: str) -> int:
        return -1

    def _maxNonAdjacentPath(self):
        pass

    def longestPath(self, parent: List[int], s: str) -> int:
        childOf = defaultdict(list)
        for i, parentIndex in enumerate(parent[1:]):
            childOf[parentIndex].append(i)
        rootChar = s[0]
        leftDepth = self._maxNonAdjacentDepth(childOf[0], childOf, s)
        rightDepth = self._maxNonAdjacentDepth(childOf[0], childOf, s)
        return 0
    

        #-----------------------------------------------
        # O(n), O(n)
        
        G = defaultdict(list)
        
        # create parent-child graph
        for i in range(1, len(parent)):
            G[parent[i]].append(i)

        res = 1

        def dfs(par):
            if not G[par]:
                return 1

            nonlocal res
            #tracks the longest valid path through the current node, 
            #allowing the parent to combine it with other paths
            accum = 1 # Initialized to 1 (just par itself).
            for chd in G[par]:
                length_of_child = dfs(chd)
                if s[chd] != s[par]:
                    res = max(res, length_of_child + accum)
                    accum = max(accum, length_of_child + 1)
            return accum
        
        dfs(0)
        return res