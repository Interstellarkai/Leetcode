#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        T : O(LogN) 71.16% | 36ms
        S : O(1) 60.16% | 13.8mb
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        return left

# @lc code=end
