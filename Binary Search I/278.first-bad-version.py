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
        Binary Search Approach
        T : O(LogN)
        S : O(1)

        mid = (start+end)) / 2;
        when start and end are all about INT_MAX , then (start+end) of course will be overflow !
        mid =  start+(end-start)/2; is a better solution
        """
        # Initialization
        left = 1
        right = n
        min = n
        while (left <= right):
            mid = (left + right)//2
            # False
            if (not isBadVersion(mid)):
                left = mid + 1
            # True
            else:
                right = mid - 1
                min = mid
        return min

# @lc code=end

