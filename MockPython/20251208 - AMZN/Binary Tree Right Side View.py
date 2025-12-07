#https://leetcode.com/problems/binary-tree-right-side-view/

from common_types import *

"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

   1
 2  3
n 5

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levelNodes = deque([root])
        rightViewValues = []
        while levelNodes:
            nodeCount = len(levelNodes)
            currNode = None
            for _ in range(nodeCount):
                currNode = levelNodes.popleft()
                if currNode.left:
                    levelNodes.append(currNode.left)
                if currNode.right:
                    levelNodes.append(currNode.right)
            if currNode:
                rightViewValues.append(currNode.val)
        return rightViewValues