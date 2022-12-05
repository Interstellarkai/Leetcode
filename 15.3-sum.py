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
        idea: sort the array, anchor with i, then use twoSumII to find the other two numbers.
        T : O(N^2) 78.67% | 1185ms
        S : O(1) 23.11% | 18.2mb
        """
        res = []
        n = len(nums)
        nums.sort()
        # used = set()
        

        for i in range(n):
            # Skip this val if it was the same as previous one.
            # This reduces complexity from O(N^3) to O(N^2)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Essentially twoSumII, but with a third pointer (i)
            left, right = i+1, n-1
            while left < right: # cannot be <= because the index has to be unique
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

                    # To avoid duplicates, we have to skip the next value that is the same as the current one
                    # Alternatively, we can use a set to store the values and check. But that is slower.
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return res

# @lc code=end

