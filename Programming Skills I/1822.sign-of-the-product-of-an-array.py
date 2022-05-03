#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#

# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Slower Approach
        """
        negCount = 0
        for ele in nums:
            if (ele == 0):
                return 0
            if (ele < 0):
                negCount += 1
        if ((negCount % 2) == 0):
            return 1
        return -1

    def arraySign(self, nums: List[int]) -> int:
        """
        Faster Approach
        """
        answer = 1
        for ele in nums:
            if (ele == 0):
                return 0
            if (ele < 0):
                answer *= -1
        return answer


# @lc code=end
