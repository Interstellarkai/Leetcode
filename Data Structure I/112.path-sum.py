#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        T : O(V+E) 22.00% | 75ms
        S : O(H) 57.50% | 15mb
        """
        # Sanity Check
        if root is None:
            return False
        # Leaf node
        if not (root.left or root.right):
            return root.val == targetSum
        # Recursion - preorder traversal
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        T : O(V+E) 99.99%
        S : O(H)
        """
        if root == None:
            return False
        targetSum = targetSum - root.val
        if (targetSum == 0) and root.left == None and root.right == None:
            return True
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Stack Method
        T : O(V+E) 43.65% | 62ms
        S : O(H) 57.50% | 15.1mb
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right and val == targetSum:
                return True
            if node.right:
                stack.append((node.right, val + node.right.val))
            if node.left:
                stack.append((node.left, val + node.left.val))
        return False
# @lc code=end
