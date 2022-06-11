#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
        """
        Helper Function
        """
        if root:
            return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        return []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        T : O(V+E) 5.00% | 655ms
        S : O(1) 13.76% | 17.2mb
        """
        if not root:
            return True
        validL, validR = True, True
        # left subtree of a node contains only nodes with keys less than the node's key.
        if root.left:
            leftSubTree = self.inOrder(root.left)
            largest = max(leftSubTree)
            validL = True if largest < root.val else False
        # right subtree of a node contains only nodes with keys greater than the node's key.
        if root.right:
            rightSubTree = self.inOrder(root.right)
            print(rightSubTree, root.val)
            smallest = min(rightSubTree)
            validR = True if smallest > root.val else False
        # Both the left and right subtrees must also be binary search trees.
        return validL and validR and self.isValidBST(root.left) and self.isValidBST(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        T : O(N) 24.89% | 77ms
        S : O(N) 13.76% | 17mb
        """
        output = self.inOrder(root, output)
        # Insertion Sort Comparison
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        T : O(V+E) 99.99% 
        S : O(H) 
        """
        def dfs(root, upper, lower):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return dfs(root=root.left, lower=lower, upper=root.val) and dfs(lower=root.val, upper=upper, root=root.right)

        return dfs(root=root, upper=float('inf'), lower=float('-inf'))


# @lc code=end
