#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Addon to twoSumII
        twoSum uses hashmap, twoSumII uses two pointers.
        T : O(N^2)
        S : O(1)
        """
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            # Skip this val if it was the same as previous one
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:  # cannot be <= because the index has to be unique
                threeSum = nums[i] + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # Continue to find other solutions that may be in the subarray
                    # We only have to update one pointer, the two other lines above will update right
                    # E.g. [-2, -2, 0, 0, 2, 2], L=0, R=5 and we want L=2 and L=3
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res

# @lc code=end
