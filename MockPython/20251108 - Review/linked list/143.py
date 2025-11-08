#https://leetcode.com/problems/reorder-list

from common_types import *

"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


1->2->3->4

1->4->2->3

1->2
4->3

first: split from middle
2nd step: reverse 2nd half
3rd step: merge the two half
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def _getMiddle(self, head) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def _reverse(self, head) ->Optional[ListNode]:
        #prev, curr, next
        #prev->curr->next
        #prev<-curr<-next
        prev = None
        curr = head
        while curr:
            # swap direction
             
            #   |0        |1
            #             |0        |1
            # [prev] -> [curr] -> [...]
            #    ^-------------|
            curr.next, prev, curr = prev, curr, curr.next
        return prev


    """
    curr1 -> next1

    curr2 -> next2

    curr1->curr2->next1->next2

    """
    def _merge(self, head1, head2):
        curr1, curr2 = head1, head2
        while curr1 and curr2:
            next1 = curr1.next
            next2 = curr2.next

            # critical move
            curr1.next = curr2
            curr2.next = next1

            # iteration transition
            curr1 = next1
            curr2 = next2

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split half
        middle = self._getMiddle(head)
        secondHead = middle.next
        middle.next = None
        reverseMiddle = self._reverse(secondHead)
        self._merge(head, reverseMiddle)