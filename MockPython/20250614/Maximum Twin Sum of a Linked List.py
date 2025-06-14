from common_types import *
#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/        

"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list
 is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

Constraints:
The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105 
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        return 0