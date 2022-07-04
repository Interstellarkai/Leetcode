#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        BFS Approach
        T : O(V+E) 19.55% | 120ms
        S : O(B) 47.26% | 15.8mb
        """
        import collections
        if not root:
            return root
        # Double ended queue, Double linked list
        queue = collections.deque([root])
        while queue:
            # To clear level by level
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if node:  # Not None
                    if i < level - 1:
                        node.next = queue[0]
                    else:
                        node.next = None

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        return root
        # if not root:
        #     return None
        # queue = [root]
        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if i < size - 1:
        #             node.next = queue[0]
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        Tree Manipulation
        T : O(V+E) 52.73% | 92ms
        S : O(D) 74.84% | 15.5mb
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
        return root

        # if not root:
        #     return None
        # if not root.left and not root.right:
        #     return root
        # root.left.next = root.right
        # if root.next:
        #     root.right.next = root.next.left
        # self.connect(root.left)
        # self.connect(root.right)
        # return root

# @lc code=end
