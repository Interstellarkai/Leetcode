#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder Traversal is first visit. Once a node is touched, print it.
        Recursive
        T : O(V+E) 63.29% | 38ms, little recursion overhead
        S : O(H) 58.51% | 13.8mb, recursive call consumes stack space
        """

        # Sanity Check
        if root is None:
            return []

        # Main
        result = []
        result.append(root.val)

        if root.left:
            result += self.preorderTraversal(root.left)
        if root.right:
            result += self.preorderTraversal(root.right)

        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Preorder Traversal is first visit. Once a node is touched, print it.

        Preorder, Inorder, Postorder
            - DFS
            - Stack -> LIFO

        Iterative
        T : O(V+E) 16.93% | 56 ms
        S : O(H) 96.64% | 13.8mb better because of less stack space
        """

        # Sanity Check
        if root is None:
            return

        # Initialize
        stack = [root]  # For tranversing
        result = []  # To store returning result

        # Main
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        # Would be faster to do this instead.
            # node = stack.pop()
            # if node:
            #     stack.append(node.right)
            #     stack.append(node.left)
            #     result.append(node.val)
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res
# @lc code=end
