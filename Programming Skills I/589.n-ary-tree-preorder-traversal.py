#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        Pre-order : <root><left><right>
        T : O(N)
        S : O(N), the max recursive depth can be N if the tree is skewed one.


        """
        # DFS Function (preorder, inorder, postorder)
        def dfs(root: 'Node', output: List[int]):
            # Terminating condition
            if root is None:
                return

            # Add in the root value
            result.append(root.val)

            # Left and right branch
            for child in root.children:
                dfs(child, result)

        # Main
        result = []
        dfs(root, result)
        return result

    def preorder(self, root: 'Node') -> List[int]:
        """
        (Iterative Approach)
        Pre-order is first visit, append

        In the iterative solution, we will maintain an explicit stack. We start by pushing the root node into the stack. We loop till stack becomes empty -

        Pop the top node - Top from the stack and insert it into result.
        Push all of the child nodes of Top into the stack from right to left. We need to push from right to left to get the right preorder traversal.
        """
        if root == None:
            return []

        # start with root in stack & loop till stack is not empty
        stack, result = [root], []

        while len(stack):
            top = stack.pop()
            result.append(top.val)   # First push the value on top
            # And then push all its children from right to left (so that leftmost would be on top & visited next)
            stack.extend(reversed(top.children))

        return result
# @lc code=end
