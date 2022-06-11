#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root: Optional[TreeNode]) -> list:
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) if root else []

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Sorted Array with 2 pointers
        T : O(N) 5.60% | 248 ms
        S : O(N) 19.50% | 20.2mb
        """
        lst = self.inOrder(root)
        left = 0
        right = len(lst) - 1
        while left < right:
            if lst[left] + lst[right] == k:
                return True
            elif lst[left] + lst[right] < k:
                left += 1
            else:
                right -= 1
        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """
        Hash Table Method
        T : O(N) 11.52% | 187ms
        S : O(N) 81.16% | 16.3mb
        """
        lst = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val in lst:
                return True
            else:
                lst.append(k-node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return False

# @lc code=end
