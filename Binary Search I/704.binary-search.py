#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Sanity Check
        if len(nums) <= 0 or target == None:
            return -1
        
        # Initialization
        min = 0 
        max = len(nums) - 1
        
        # Main
        while (min <= max):
        
            mid = (min + (max-min)//2)
        
            if target == nums[mid]:
                return mid
            
            # Target is smaller
            if target < nums[mid]:
                max = mid - 1
            
            # Target is bigger
            else:
                min = mid + 1
        
        return -1
# @lc code=end

