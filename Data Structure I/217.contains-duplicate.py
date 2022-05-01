#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set function to eliminate duplicates
        distinct = set(nums)
        # Compare len of original and distinct
        return (len(distinct) != len(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:

        # Use dictionary, {key : val} pair to identify duplicates
        # T: O(N)
        # S: O(N)

        dict = {}

        for num in nums:
            if num in dict:
                # dict[key] = val
                dict[num] += 1
            else:
                dict[num] = 1

        for k, v in dict.items():
            if v > 1:
                return True

        return False
# @lc code=end
