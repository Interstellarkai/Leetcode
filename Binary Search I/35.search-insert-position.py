#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Sanity Check
        if (nums == None):
            return -1

        # Initialize
        min = 0
        max = len(nums) - 1

        while (min <= max):
            mid = (min + (max - min)//2)

            # Found
            if (target == nums[mid]):
                return mid
            # Move left
            elif (target < nums[mid]):
                max = mid-1
            # Move right
            else:
                min = mid+1

        # Default : return the suppose index location
        return min
# @lc code=end
