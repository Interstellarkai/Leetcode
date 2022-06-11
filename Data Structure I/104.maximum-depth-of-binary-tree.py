#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from urllib.parse import non_hierarchical


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursion approach
        T : O(V+E) 57.75% | 54ms
        S : O(H) + Call Stacks 22.70% | 16.3mb
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Iterative DFS approach
        Using Stack
        T: O(V+E) 48.52% | 58ms
        S: O(H) 89.96% | 15.3mb
        """
        # Sanity Check
        if root is None:
            return 0
        # Initialize
        stack = [(root, 1)]
        max_depth = 0
        # Main
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
            # This method will yields '+1' another time because stacks has none as child nodes
            # if node:
            #     stack.append((node.right, depth + 1))
            #     stack.append((node.left, depth + 1))
        return max_depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS approach
        Using Queue
        T: O(V+E) 9.85% | 83ms
        S: O(L) 98.72% | 15.2mb
        """
        # Sanity Check
        if root is None:
            return 0
        # Initialize
        max_depth = 0
        queue = [root]
        # Main
        while queue:
            max_depth += 1
            for _ in range(len(queue)): # Clear level at this time capture (cannot do for node in queue)
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left) # Append next level child nodes
                if node.right:
                    queue.append(node.right) # Append next level child nodes
        return max_depth

# @lc code=end

