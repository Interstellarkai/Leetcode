#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    """
    Binary Search
    T : O(LogN)
    S : O(1)
    """

    def mySqrt(self, x: int) -> int:
        # Initialize
        left = 0
        right = x

        while (left <= right):
            mid = left + (right - left)//2

            # N.b.: Condition cannot be exact, but within a range
            if (mid**2 <= x < (mid+1)**2):
                return mid
            elif (x < mid**2):
                right = mid - 1
            else:
                left = mid + 1


# @lc code=end
