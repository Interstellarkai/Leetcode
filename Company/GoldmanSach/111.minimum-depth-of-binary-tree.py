#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Queue method - BFS
        T : O(B) 13.28% | 1097ms
        S : O(N) 62.77% | 49.5mb
        """
        if not root:
            return 0

        from collections import deque
        queue = deque([[root]])
        depth = 0

        while queue:
            nextLevel = []
            level = queue.popleft()
            depth += 1
            for node in level:
                # Terminating Case
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                queue.append(nextLevel)

        return depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Queue method - BFS (Binary Tree so breadth is good)
        T : O(B) 35.66% | 913ms
        S : O(N) 79.49% | 49.4mb
        """
        if not root:
            return 0

        queue = collections.deque([(root, 1)])

        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursion method - DFS (Can be very skewed)
        T : O(D) 8.27% | 1165ms
        S : O(N) 8.93% | 55.2mb
        """
        if not root:
            return 0

        # Terminating Case
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        # Recursion
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# @lc code=end
