#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Started off by reading the tag that it was binary search.
        Written a template of binary search followed by deliberating how it will fit into the context

        T: O(LogN)
        S: O(1)
        """
        # Initialize
        low = 0
        high = num

        while (low <= high):
            mid = low + (high-low)//2

            if (mid**2 == num):
                return True
            elif (mid**2 < num):
                low = mid+1
            else:
                high = mid-1

        return False

# @lc code=end
