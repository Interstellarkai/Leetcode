#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder traversal is second visit: nodes needs to be touched twice before printing.
        Recursive (main is between 2 recursive call)
        T : O(V+E) 10.95% | 60ms 
        S : O(H) 59.36% | 13.9mb recursive call consumes stack space
        """
        # Sanity Check
        if root is None:
            return []

        # Initialize
        result = []
        # Recursive 1
        if root.left:
            result += self.inorderTraversal(root.left)
        # Main
        result += root.val
        # Recursive 2
        if root.right:
            result += self.inorderTraversal(root.right)

        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.preorderTraversal(root.right) if root else []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder traversal is second visit: nodes needs to be touched twice before printing.

        Preorder, Inorder, Postorder
            - DFS
            - Stack -> LIFO

        Iterative
        T : O(V+E) 74.07% | 33ms
        S : O(H) 96.83% | 13.8ms
        """
        # Sanity Check
        if root is None:
            return []

        # Initialize
        stack = []
        result = []
        node = root
        # Main
        while stack or node:
            # Expand always left
            if node:
                stack.append(node)
                node = node.left
            else:
                # Expand always riht
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/713539/Python-3-All-Iterative-Traversals-InOrder-PreOrder-PostOrder-Similar-Solutions
        T : O(V+E) 18.59% | 55ms
        S : O(H) 59.36% | 13.9mb
        """
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

# @lc code=end
