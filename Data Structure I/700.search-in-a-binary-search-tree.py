#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from jmespath import search


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Recursion
        T : O(LogN) 14.46% | 116ms
        S : O(H) 63% | 16.5mb
        """
        if not root:
            return None
        elif root.val == val:
            return root
        else:
            return self.searchBST(root.left, val) or self.searchBST(root.right, val)
        
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Stack
        T : O(LogN)) 65.93% | 81ms
        S : O(H) 17.81% | 16.5mb
        """
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == val:
                    return node
                elif val < node.val:
                    stack.append(node.left)
                else:
                    stack.append(node.right)
        return None
    
    def searchBST(self, root, val):
        """
        Binary Search Tree (Binary Search means left small, right big)
        T : O(LogN)
        S : O(H)
        """
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root
# @lc code=end
