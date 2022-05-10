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
        Ref : https://www.youtube.com/watch?v=GfRQvf7MB3k
        T : O(m + n) => 66ms
        S : O(1)
        """
        # Sanity Check
        # If one of them is empty, return the other
        if None in (list1, list2):
            return list1 or list2

        # Dummy sits at the start of the linked list
        # Cur is going to move forward to find which value should be added to the list.
        dummy = cur = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next

            else:
                cur.next = list2
                list2 = list2.next

            # Default : Cur has to move forward (Tail of dummy) to
            cur = cur.next

        # One of the list is empty, but still got another node
        cur.next = list1 or list2
        return dummy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Ref : https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained
        T : O(N) => 32ms
            - T (N-1) + 1 -> Master Theorem to O(N)
        S : O(m + n)
        """
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
