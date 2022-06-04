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
    ########################################################################
    ############################### RECURSIVE ##############################
    """
    https://leetcode.com/problems/reverse-linked-list/discuss/1711202/Detailed-explanation-of-recursive-solution-%2B-alternate-simpler-recursive-solution
    For anyone still trying to understand the recursive solution, here's the step by step explanation, considering the example given in the question:

    1 -> 2 -> 3 -> 4 -> 5

    For the first 4 calls of the reverseList function, we just go into the call stack, as the base case is not hit. When we call the function for the 5th time, that is, reverseList(5), we reach the base case as 5.next == null, so we return at this point to the 4th call in the stack, that is, reverseList(4). Now, for this 4th node, p is set equal to the returned value (5th node) and essentially this is the only time p gets updated in the whole solution. After this point, p's value is just passed across stack calls so that it can be returned as the new head.
    Back to the next line in the 4th stack call, head.next.next = head. This line simply means, make the next node of the current node, point to the current node. So, 5.next is set equal to 4th node.
    Next line says, head.next = null and this seems a bit confusing but it really isn't. This line has no significance for any other node except the (new) last one, that is, for the node containing 1 as value. This statement is just used to set the value of 1.next as null. For all other nodes, this line means nothing as it gets overwritten as we move back further in the call stack. Let's understand by going further in the example:
    So, at this point, we have p = 5, 5.next = 4, 4.next = null, and now we move back in the call stack to reverseList(3). Here again we have head.next.next = head, which basically means, 4.next = 3. So you see, the head.next = null had no impact on the 4th node as it was updated in the next call. Going forward in a similar manner, you will observe, the value set by head.next = null gets overwritten for every node except for the first one, where there's no next call to update it, which mean, 1.next = null, which is what we want in the final linked list.
    Lastly, every stack call returns p which was just set in the last call when we were going in (p = 5) and as I said before, it doesn't get updated in any call after that, so it just serves to return the new head of the reversed list.

    Hope this makes it clearer for you. If you still find the recursive solution difficult to understand, I have an alternative recursive solution which uses 2 variables as a substitute to head.next.next, which may seem easier:
    """


class Solution:
    def flipMapping(self, curr, nex):
        if nex.next:
            self.flipMapping(curr.next, nex.next)
        else:
            self.new_head = nex

        nex.next = curr

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        self.new_head = None
        self.flipMapping(head, head.next)
        head.next = None
        return(self.new_head)

# @lc code=end
