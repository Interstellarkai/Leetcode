#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/product-of-array-except-self/discuss/1610450/Attention-No-One-Going-to-Explain-like-this
        Using [left to right], [right to left] method
        T : O(N) 36.69% | 389ms
        S : O(N) 7.68% | 23.4mb => Excluding output array
        """
        # Initialize
        left_to_right = [1] * len(nums)
        right_to_left = [1] * len(nums)
        res = [1] * len(nums)

        # Left to right
        for i in range(1, len(nums)):
            left_to_right[i] = left_to_right[i-1] * nums[i-1]
        # Right to left
        for i in range(len(nums)-2, -1, -1):
            right_to_left[i] = right_to_left[i+1] * nums[i+1]

        # Compute result
        for i in range(len(nums)):
            res[i] = left_to_right[i] * right_to_left[i]

        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Same as above.
        Attempt to get O(1) for space complexity
        T : O(N) 75.13% | 280ms
        S : O(N) 38.06% | 21.4mb => Excluding output array
        """
        # Initialize
        n = len(nums)
        left_to_right = [1] * n

        # Left to right
        for i in range(1, n):
            left_to_right[i] = left_to_right[i-1] * nums[i-1]

        # Compute result
        right_to_left = 1  # Right to left
        for i in range(1, n+1):
            left_to_right[-i] *= right_to_left
            right_to_left *= nums[-i]  # Right to left

        return left_to_right
# @lc code=end
