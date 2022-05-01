#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:  # Loop till n is 0
            n &= n-1  # operator returns the intersect between the 2 vals
            count += 1
        return count
# @lc code=end
