#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursion
        T : O(V+E) 21.06% | 54ms
        S : O(H) 60.82% | 13.8mb
        """
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative
        T : O(V+E) 92.34% | 24ms
        S : O(H) 13.48% | 14mb
        """
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return res
# @lc code=end
