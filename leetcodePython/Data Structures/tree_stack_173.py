#https://leetcode.com/problems/binary-search-tree-iterator/description/
# Input
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output
# [null, 3, 7, true, 9, true, 15, true, 20, false]

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = 0
        self.inorder = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.inorder.append(root.val)
            inorder(root.right)
        inorder(root)
        
    def next(self) -> int:
        self.curr+=1
        return self.inorder[self.curr - 1]

    def hasNext(self) -> bool:
        return self.curr < len(self.inorder)
    
class BSTIterator_opt:
    def __init__(self, root: TreeNode) -> None:

        # Stack for the recursion simulation
        self.stack = []

        # Remember that the algorithm starts with a call to the helper function
        # with the root node as the input
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root: TreeNode) -> None:

        # For a given node, add all the elements in the leftmost branch of the tree
        # under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        # Node at the top of the stack is the next smallest element
        top_node = self.stack.pop()

        if top_node.right:
            self._leftmost_inorder(top_node.right)

        return top_node.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0