#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Simple Approach
        T : O(NLogN) 26.99% | 387ms
        S : O(1) 97.31% | 15.7mb
        """
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        T : O(N) 20.25% | 416ms
        S : O(N) 49.97% | 16.3mb
        """
        res = [None] * len(nums)
        counter = len(nums)-1
        left, right = 0, len(nums)-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[counter] = nums[left]**2
                counter -= 1
                left += 1
            else:
                res[counter] = nums[right]**2
                counter -= 1
                right -= 1
        return res

    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Similar to 2nd approach, two pointers.f
        """
        result = [None] * len(nums)
        left, right = 0, len(nums) - 1
        # Start (inclusive), End (exclusive), Steps
        for index in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
        return result

# @lc code=end
