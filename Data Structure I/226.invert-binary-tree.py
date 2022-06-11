#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        DFS - Pre-order traversal - Stack
        T : O(V+E) 5.30% | 69ms 
        S : O(H) 55.39% | 13.8mb
        """
        if root is None:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            # # This is faster 23.67% | 54ms
            # if node.left:
            #     stack.append(node.left)
            # if node.right:
            #     stack.append(node.right)
            if node:
                # pre-order transversal
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursion
        T : O(V+E) 82.35% | 34ms 
        S : O(H) 55.39% | 13.9mb
        """
        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursion
        T : O(V+E) 99.99%
        S : O(H)
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
# @lc code=end
