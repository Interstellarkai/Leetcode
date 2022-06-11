#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Concept: Breadth First Search, requires a Queue
        T : O(V+E) 17.73% | 64ms
        S : O(L) 83.11% | 14.1mb
        """
        # Sanity Check
        if not root:
            return []

        # Initialize
        result, queue = [], [root]

        while queue:
            level = []
            for _ in range(len(queue)):  # Explore current level
                node = queue.pop(0)  # dequeue current level node
                level.append(node.val)
                if node.left:
                    queue.append(node.left)  # enqueue child node
                if node.right:
                    queue.append(node.right)  # enqueue child node
            # Insert this level to result
            result.append(level)
        return result

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        We should not use pop(0), therefore it costs O(n).
        T : O(V+E) 46.19% | 50ms
        S : O(L) 83.11% | 14.1mb
        """
        if not root:
            return []

        result: List[List[int]] = []
        lay = [root]
        while lay:
            lay_values = []
            next_lay = []

            for node in lay:
                lay_values.append(node.val)
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)

            lay = next_lay
            result.append(lay_values)

        return result
# @lc code=end
