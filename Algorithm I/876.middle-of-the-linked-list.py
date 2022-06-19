#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Simple Approach
        T : O(N) 19.94% | 56ms
        S : O(1) 54.31% | 13.8mb
        """
        # Sanity Check
        if head is None:
            return None
        if head.next is None:
            return head

        # Get the length
        cur = head
        length = 1
        while cur.next is not None:
            length += 1
            cur = cur.next

        # Get the mid
        mid = length // 2
        cur = head
        while mid:
            mid -= 1
            cur = cur.next
        return cur

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/middle-of-the-linked-list/discuss/526372/Python-O(n)-by-two-pointers-90%2B-w-Diagram
        Two Pointers
        Fast pointer will move two times ahead of Slow pointer
        T : O(N) 18.03% | 57ms
        S : O(1) 10.42% | 13.9mb
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            # fast has reached the end of linked list
            # slow is on the middle point now
            fast = fast.next.next
        return slow

# @lc code=end
