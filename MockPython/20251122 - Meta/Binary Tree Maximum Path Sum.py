#https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

from common_types import *

"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:

  1
 / \
2   3

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

1
 \
 -10
9   20
   15 7

   



Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _postOrderPathSum(self, node) -> float:
        if not node:
            return 0
        leftTreeSum = max(0, self._postOrderPathSum(node.left))
        rightTreeSum = max(0, self._postOrderPathSum(node.right))
        self._maxPathSum = max(self._maxPathSum, node.val + leftTreeSum + rightTreeSum)
        return node.val + max(leftTreeSum, rightTreeSum)

    def maxPathSum(self, root: Optional[TreeNode]) -> float:
        self._maxPathSum = float('-inf')
        self._postOrderPathSum(root)
        return self._maxPathSum