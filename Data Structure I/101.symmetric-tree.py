#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left_node, right_node):
            if not left_node and not right_node:
                return True
            
            if not left_node or not right_node:
                return False
            
            if left_node.val != right_node.val:
                return False
            
            return dfs(left_node.left, right_node.right) and dfs(left_node.right, right_node.left)
        
        return dfs(root, root)




    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Iterative DFS approach
        Using Stack
        T: O(V+E) 36.80% | 53ms
        S: O(L) 93.90% | 13.9mb
        """
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            # Check
            if left is None and right is None:
                continue
            # Check
            if left is None or right is None:
                return False
            # Check
            if left.val != right.val:
                return False
            # Appending
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        return True


# @lc code=end
