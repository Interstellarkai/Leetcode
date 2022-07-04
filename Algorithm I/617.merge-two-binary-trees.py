#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive Method
        T : O(V+E)
        S : O(H)
        Time complexity : O(m). 
            A total of m nodes need to be traversed. 
            Here, m represents the minimum number of nodes from the two given trees.
        Space complexity : O(m). 
            The depth of the recursion tree can go upto m in the case of a skewed tree.
            In average case, depth will be O(logm).
        """
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            res = TreeNode(root1.val + root2.val)
            res.left = self.mergeTrees(root1.left, root2.left)
            res.right = self.mergeTrees(root1.right, root2.right)
        return res

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursive Method
        T : O(V+E)
        S : O(H)

        1. If both trees are empty then we return empty.
        2. Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
        3. The left child will be the merge of root1.left and root2.left, except these trees are empty if the parent is empty.
        4. The right child is similar.
        """
        if not root1 and not root2:
            return None
        ans = TreeNode((root1.val if root1 else 0) +
                       (root2.val if root2 else 0))
        ans.left = self.mergeTrees(root1 and root1.left, root2 and root2.left)
        ans.right = self.mergeTrees(
            root1 and root1.right, root2 and root2.right)
        return ans

# @lc code=end
