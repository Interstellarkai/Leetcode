#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Simple Approach
        T : O(N) 5.60% | 77ms
        S : O(1) 68.61% | 13.9mb
        """
        if head is None:
            return head
        # Get the size of linked list
        cur = head
        size = 1
        while cur.next:
            size += 1
            cur = cur.next

        # Removal
        removal_index = size - n
        cur_index = 1
        cur = head

        # If Removal of head
        if removal_index == 0:
            head = cur.next
            return head

        # If there is a need to transverse
        while cur_index < removal_index:
            cur_index += 1
            cur = cur.next
        cur.next = cur.next.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two Pointers
        Concept:
            The difference between the fast and slow pointer is "n-1".
            Distinct the difference first, then transverse to the end.
        T : O(N) 87.05% | 36ms
        S : O(1) 68.61% | 13.9mb
        """
        fast = slow = head
        # Distinct the difference by n
        for _ in range(n):
            fast = fast.next
        # If removal is at the start of the head, first node
        if not fast:
            return head.next
        # Transver to the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        # Removal
        slow.next = slow.next.next
        return head


# @lc code=end
