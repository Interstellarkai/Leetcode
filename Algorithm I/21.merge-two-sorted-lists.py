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
        Sorted List
        T : O(N) 74.13% | 46 ms
        S : O(1) 31.85% | 13.9ms
        """
        res = cur = ListNode()  # Res is a temp ptr for the new res head, cur for transversal
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next = list1  # Point to new node
                    cur = cur.next  # Moving forward
                    list1 = list1.next  # Update list
                else:
                    cur.next = list2  # Point to new node
                    cur = cur.next  # Moving forward
                    list2 = list2.next
            elif list1 and not list2:  # Append all to the res list
                cur.next = list1  # Update list
                break
            else:
                cur.next = list2  # Append all to the res list
                break
        return res.next

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
