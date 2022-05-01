#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        Idea: One of the side should not be greater than the sum of the other 2 sides
        T : O(NLogN)
        S : O(N)
        """

        # Descending order
        # nums.sort(reverse = True) # Inplace sort S : O(1) | T : O(NLogN)
        # New list     S : O(N) | T : O(NLogN) -> But faster
        nums = sorted(nums)[::-1]

        # enumerate until the last 2 val
        # for i, val in enumerate(nums[:-2]):
        for i in range(len(nums) - 2):
            # Check based on idea
            if (nums[i] < (nums[i+1] + nums[i+2])):
                return (nums[i] + nums[i+1] + nums[i+2])

        return 0

# @lc code=end
