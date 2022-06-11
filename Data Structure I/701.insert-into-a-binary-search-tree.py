#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        T : O(LogN) 29.90% | 209ms
        S : O(H) 9.59% | 17mb
        """
        # Left
        if root and val < root.val:
            # Slot taken
            if root.left:
                self.insertIntoBST(root.left, val)
                return root
            # Empty slot
            else:
                root.left = TreeNode(val)
                return root
        # Right
        if root and val > root.val:
            # Slot taken
            if root.right:
                self.insertIntoBST(root.right, val)
                return root
            # Empty slot
            else:
                root.right = TreeNode(val)
                return root
        else:
            return TreeNode(val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        T : O(LogN) 28.54% | 212ms
        S : O(H) 92.69% | 16.8mb # Each call is O(1) * Max Depth H, recursions
        """
        if (root == None):
            return TreeNode(val)
        if (root.val < val):
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
# @lc code=end
