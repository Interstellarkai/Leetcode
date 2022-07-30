#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Bruteforce approach
        T : O(N^2)
        S : O(1)
        """

        # Initialize
        maxVal = -999

        # Take one of the val and anchor it
        for i in range(len(nums)):
            anchoredVal = nums[i]
            # Update if the taken val is already greater than maxVal
            if (maxVal < anchoredVal):
                maxVal = anchoredVal

            # Number of shifts remaining towards the right after anchoring
            remainingshift = (len(nums) - i - 1)

            # Loop thru the remaining val
            for r in range(remainingshift):
                incrementedVal = nums[i + r + 1]
                anchoredVal += incrementedVal

                # Update if the new combination is greater than maxVal
                if (maxVal < anchoredVal):
                    maxVal = anchoredVal

        return maxVal

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Dynamic programming approach: Kadane's approach
        T: O(N) 36.7% | 1164ms
        S: O(1) 77.95% | 27.8mb
        """
        # Initialize
        currSum = maxVal = nums[0]

        # Linear loop through the array
        for num in nums[1:]:
            # Is it more worth it to continue, or is it better to start afresh with the new num
            currSum = max(num, currSum + num)
            # Check back and update maxVal
            maxVal = max(maxVal, currSum)
        return maxVal

# @lc code=end
