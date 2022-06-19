#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        """
        T : O(N^2) 5.65% | 1700ms
        S : O(1) 63.33% | 15.5mb
        """
        for element in nums:
            if element == 0:
                nums.remove(element)  # O(N) operation, arg: value
                nums.append(0)

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two Pointers
        T : O(N^2) 70.91% | 192ms
        S : O(1) 15.91% | 15.7mb
        """
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] == 0:
                nums.pop(left)  # O(N) operation, arg: index
                nums.append(0)  # arg: value
                right -= 1
            else:
                left += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Two Pointers with swap
        T : O(N) 53.45% | 233ms
        S : O(1) 63.33% | 15.6mb
        """
        zero_index = 0  # first zero's index
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1

# @lc code=end
