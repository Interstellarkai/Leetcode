#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        One Pass
        T : O(N) 34.96% | 1132 ms
        S : O(1) 73.22% | 30 mb
        """
        # Sanity check
        if len(nums) < 3:
            return False
        # Idea: Traverse the array, keep track of the smallest and second smallest
        smallest = second_smallest = float("inf")
        for idx in range(len(nums)):
            cur = nums[idx]
            # Terminating clause
            if smallest < cur and second_smallest < cur:
                return True
            # To update the smallest value
            elif cur < smallest and cur < second_smallest:
                smallest = cur
            # To update the second_smallest value
            elif cur > smallest and cur < second_smallest:
                second_smallest = cur
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        One Pass (Refactor)
        T : O(N) 84.33% | 1049 ms
        S : O(1) 24.71 | 30.1 mb
        """
        # Sanity check
        if len(nums) < 3:
            return False
        # Idea: Traverse the array, keep track of the smallest and second smallest
        first = second = math.inf
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # Now first < num, if num <= second then try to make `second` as small as possible
                second = num
            else:  # Now first < second < num
                return True
        return False

# @lc code=end
