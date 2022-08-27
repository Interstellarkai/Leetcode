#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        T : O(N) 13.91% | 77ms
        S : O(N) 79.49% | 13.9mb
        """
        head = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                # Add smaller value
                cur.next = list1
                # Update pointer
                list1 = list1.next
            else:
                # Add smaller value
                cur.next = list2
                # Update pointer
                list2 = list2.next
            cur = cur.next

        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next

        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next

        return head.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Sanity check
        if not list1 or not list2:
            return list1 or list2

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
# @lc code=end
