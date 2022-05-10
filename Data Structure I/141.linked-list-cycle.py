#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Similar to Leetcode 202.
        Track if node has been visited before using (val, ptr) for node representation.
        T : O(N^2) => 91ms
        S : O(N)
        """
        # Sanity check
        if head == None or head.next == None:
            return False

        # Initialize
        visited = set()
        visited.add(head.val)
        ptr = head.next

        # Transverse through the linked list
        while ptr != None:
            # Check if node visited before
            if (ptr.val, ptr.next) in visited:
                print((ptr.val, ptr.next), visited)
                return True
            # Standard procdure, add and move to next node
            visited.add((ptr.val, ptr.next))
            ptr = ptr.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Bunny Method for convergence
        Approach: Floyd's Cycle-Finding Algorithm
        T : O(LogN) => 73ms
        S : O(1)

        Intuition
        The chain we get by repeatedly calling getNext(n) is an implicit LinkedList. 
        Implicit means we don't have actual LinkedNode's and pointers,
        but the data does still form a LinkedList structure. 
        The starting number is the head "node" of the list,
        and all the other numbers in the chain are nodes.
        The next pointer is obtained with our getNext(n) function above.

        Recognizing that we actually have a LinkedList, 
        This algorithm is based on 2 runners running around a circular race track, 
        a fast runner and a slow runner.

        Regardless of where the tortoise and hare start in the cycle,
        they are guaranteed to eventually meet. 
        This is because the hare moves one node closer to the tortoise (in their direction of movement) each step.
        """
        # Sanity check
        if head == None or head.next == None:
            return False

        # Main
        slow_runner = head
        fast_runner = head.next
        while slow_runner != fast_runner:
            # slow runner will move once
            slow_runner = slow_runner.next
            # fast runner will move twice (Easier to ask for forgiveness than permission)
            try:
                fast_runner = fast_runner.next.next
            except:
                return False
        return True
# @lc code=end
