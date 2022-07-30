#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Dynamic programming
        T : O(N^2) Exceed Time Limit
        S : O(1)
        """
        maxSum = nums[0]
        start = 0
        for end in range(len(nums)):
            subarray = sum(nums[start:end+1])  # T(N)
            maxSum = max(maxSum, subarray)
            if nums[end] > subarray:
                start = end
                maxSum = max(maxSum, nums[end])
        return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Dynamic programming
        T : O(N) 40.52% | 1164ms
        S : O(1) 78.04% | 27.8mb
        """
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSum = max(maxSum, nums[i])


# @lc code=end
