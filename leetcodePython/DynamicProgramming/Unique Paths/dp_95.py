#https://leetcode.com/problems/unique-binary-search-trees-ii/description/
# combinations of unique BST
# Example: n = 3
# Output: [[1,null,3,2],[3,2,null,1],[3,1,null,null,2],[2,1,3],[1,null,2,null,3]]
# Explanation: there are five unique BST's that store values 1 to 3

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]: