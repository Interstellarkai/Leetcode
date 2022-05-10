#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Re-routing approach
        T : O(N) => 102ms
        S : O(1)
        """
        # Sanity Check
        # if head == None:
        #     return head

        # Initialize
        dummy = cur = ListNode(0)

        # Main
        # Dummy always points to the head, Cur is the one transversing
        while head != None:
            if head.val != val:
                cur.next = head
                cur = cur.next

            # default
            head = head.next
        # Remove any remmants. I.e. linked elements from the last cur node
        cur.next = None
        return dummy.next

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Ref : https://leetcode.com/problems/remove-linked-list-elements/discuss/158651/Simple-Python-solution-with-explanation-(single-pointer-dummy-head).
        From discussion. Double pointer approach with inplace
        T : O(N) => 
        S : O(1)
        """
        prev_node = None
        curr_node = head

        while curr_node:
            if curr_node.val == val:
                # need to delete current node
                if curr_node == head:
                    curr_node = head = head.next
                else:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
            else:
                # go next
                prev_node = curr_node
                curr_node = curr_node.next

        return head

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Recursion Approach
        T : O(N) => 109ms
        S : O(N)
        """
        if (head == None):
            return None

        head.next = self.removeElements(head.next, val)

        return head.next if head.val == val else head


# @lc code=end
