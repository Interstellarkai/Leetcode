#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse Linked List
        T : O(N) 80.33% 
        S : O(1) 94.13%
        """
        # Sanity Check
        if head == None:
            return head

        # Initialize
        cur = head
        prev = None

        # Main
        while cur:
            # Save next node
            next_node = cur.next
            # Reverse the link
            cur.next = prev
            # Move prev and cur
            prev = cur
            cur = next_node
        return prev

    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
# @lc code=end
