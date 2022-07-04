#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        LSB
        T : O(1) 37.23% | 52ms
        S : O(1) 50.21% | 13.8mb
        """
        count = 0
        while n:
            count += n & 1  # LSB
            n >>= 1  # Shift right by 1
        return count

    def hammingWeight(self, n: int) -> int:
        """
        T : O(1) 96.28% | 29ms
        S : O(1) 7.78% | 13.9mb
        """
        count = 0
        while n:
            n &= n-1  # this will take out the right-most 1 of n
            count += 1
        return count
# @lc code=end
