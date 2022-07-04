#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Bitwise Manipulation
        T : O(N) 29.13% | 253ms
        S : O(1) 50.42% | 16.7mb
        """
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
        return res
# @lc code=end
