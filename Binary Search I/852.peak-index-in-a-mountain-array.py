#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Intialize
        left = 0
        right = len(arr)-1

        while (left <= right):
            mid = (left + right)//2
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid - 1

        return left

# @lc code=end

