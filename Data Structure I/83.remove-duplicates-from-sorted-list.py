#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        T: O(N) 5.14%
        S: O(1) 70.35%
        """
        # Sanity Check
        if head is None:
            return head

        # Initialize
        cur = head

        # Main
        while cur.next is not None:
            # If next node is the same val
            if cur.val == cur.next.val:
                cur.next = cur.next.next  # go to the next node
            else:
                cur = cur.next
        return head

# @lc code=end
