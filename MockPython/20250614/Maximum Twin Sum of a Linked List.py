from common_types import *
#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/        

"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list
 is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

In-place processing, no new data structures.

Constraints:
The number of nodes in the list is an even integer in the range [2, 10^5].
1 <= Node.val <= 10^5 

O(n), O(1)

[1,2,3,4,5,6]
 l         r

[1,2,3,6,5,4]
O(n) for each operation => O(n^2)

"""
class Solution:
    # [1,2,3,4] -> (1, 1) -> (2, 3) -> (3, null)
    def _getMiddle(self, head: Optional[ListNode]) -> ListNode:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # prev -> curr -> next
    # next -> curr -> prev
    #         curr.next
    def _reverse(self, head: Optional([ListNode])) -> ListNode:
        curr, prev = head, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next        
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        secondHead = self._getMiddle(head)
        # reverse secondHead
        reverseSecondHead = self._reverse(secondHead)

        head1, head2 = head, reverseSecondHead
        maxSum = 1
        while head2:
            maxSum = max(maxSum, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next
        return maxSum