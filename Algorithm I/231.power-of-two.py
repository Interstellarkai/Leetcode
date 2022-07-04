#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        Binary Search
        T : O(LogN) Time Limit Exceeded
        S : O(1)
        """
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            if 2**mid == n:
                return True
            elif 2**mid < n:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Modulus
        T : O(LogN)
        S : O(1)
        """
        if (n == 0):
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
        return True

    def isPowerOfTwo(self, n: int) -> bool:
        """
        Bit-wise Manipulation
            E.g. n = 8(1000b), n - 1 = 7(0111b) => n & n-1 == 0.
        T : O(1) 67.50% | 43ms
        S : O(1) 8.63% | 13.9mb
        """
        return (n > 0) and (n & (n - 1)) == 0
# @lc code=end
