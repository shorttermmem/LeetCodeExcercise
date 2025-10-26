# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another

from common_types import *

"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _getLCA(self, currNode:TreeNode, val1, val2) -> Optional[TreeNode]:
        if not currNode:
            return None
        if currNode.val == val1 or currNode.val == val2:
            return currNode
        leftAncestor = self._getLCA(currNode.left, val1, val2)
        rightAncestor = self._getLCA(currNode.right, val1, val2)
        if leftAncestor and rightAncestor:
            return currNode
        if leftAncestor:
            return leftAncestor
        return rightAncestor

    def _dfsGetPath(self, currNode, val, path):
        if not currNode:
            return False
        path.append("L")
        if self._dfsGetPath(currNode.left, val, path):
            return True
        path.pop()
        path.append("R")
        if self._dfsGetPath(currNode.right, val, path):
            return True
        path.pop()
        return False


    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        lca = self._getLCA(root, startValue, destValue)
        leftPath, rightPath = [], []
        self._dfsGetPath(lca, startValue, leftPath)
        self._dfsGetPath(lca, destValue, rightPath)
        fullPath = []
        fullPath.extend("U"*len(leftPath))
        fullPath.extend(rightPath)
        return "".join(fullPath)
