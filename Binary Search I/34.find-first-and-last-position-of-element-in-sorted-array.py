#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        T : O(LogN)
        S : O(1)
        """
        # Sanity check
        if len(nums) == 0:
            return [-1, -1]

        # Move left pointer to start of target
        def binarySearchLeft(nums: List[int], target: int) -> int:
            # Initialize
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        # Move right pointer to end of target
        def binarySearchRight(nums: List[int], target: int) -> int:
            # Initialize
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        # main
        leftptr = binarySearchLeft(nums, target)
        rightptr = binarySearchRight(nums, target)
        return [leftptr, rightptr] if (leftptr <= rightptr) else [-1, -1]
# @lc code=end
