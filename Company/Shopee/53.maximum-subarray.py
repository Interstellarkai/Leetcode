#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Dynamic Programming
        Thought Process: 
            1. Try to avoid negative number
            2. Is it better to continue, or start afresh here
            3. Let's try inplace addition of the current max
        T : O(N) 7.97% | 1607ms
        S : O(1) 78.24% | 29.7mb
        """
        n = len(nums)
        maxSum = nums[0]

        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSum = max(maxSum, nums[i])

        return maxSum

    def maxSubArray(self, nums: List[int]) -> int:
        """
        T : O(N) 12.95% | 1495ms
        S : O(1) 78.24% | 27.8mb
        """
        n = len(nums)
        currSum = maxSum = nums[0]

        for i in range(1, n):
            currSum += nums[i]  # Continue
            currSum = max(currSum, nums[i])  # Which is more worth doing
            maxSum = max(maxSum, currSum)  # Update global res
        return maxSum

# @lc code=end
