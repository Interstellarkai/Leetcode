#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Simple Approach
        T : O(N^3) Time limit exceeded
        S : O(N)
        """
        if len(nums) < 3:
            return None
        res = set()
        nums.sort()
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return [list(i) for i in res]
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Two Pointers
            Approach : Similar to insertion sort
        """
        # Organize
        res = set()
        nums.sort()

        for i in range(len(nums)):
            left, right = i+1, len(nums)
            while left < right: # cannot be <= because the index has to be unique
                if nums[i] + nums[left] + nums[right] == 0:
                    res.add((nums[i], nums[left], nums[right]))
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1 
            return [list(i) for i in res]


# @lc code=end
