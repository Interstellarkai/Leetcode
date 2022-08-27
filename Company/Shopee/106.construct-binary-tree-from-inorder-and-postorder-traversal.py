#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        ref : https://www.youtube.com/watch?v=s5XRtcud35E
        T : O(N^2) 51.39% | 197ms
        S : O() 38.20% | 53.8mb
        """
        # postorder = [left, right, root]
        # inorder = [left, root, right]

        # Sanity check
        if not inorder or not postorder:
            return None

        # Root can be foind in the last val of postorder
        root = postorder.pop()
        tree = TreeNode(root)

        # Get the index of the root to do inorder splicing
        rootIndex = inorder.index(root)  # O(N)
        leftSubTree = inorder[:rootIndex]
        rightSubTree = inorder[rootIndex+1:]

        # Must do right then left bc of postorder (left, right, root)
        tree.right = self.buildTree(
            rightSubTree, postorder)  # O(N/2) for T and S
        tree.left = self.buildTree(
            leftSubTree, postorder)  # O(N/2) for T and S

        return tree

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/A-better-Python-solution
        Approach: Using binary search for left and right subtree (inorder)
        T : O(N)
        S : O(N)
        """
        map_inorder = {val: idx for idx, val in enumerate(inorder)}  # O(N)

        def recur(low, high):
            if low > high:
                return None
            tree = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            tree.right = recur(mid+1, high)  # O(N/2)
            tree.left = recur(low, mid-1)  # O(N/2)
            return tree

        return recur(0, len(inorder)-1)

# @lc code=end
