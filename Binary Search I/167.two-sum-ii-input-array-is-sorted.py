#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Binary Search
        T : O(LogN) 52.43%
        S : O(1) 11.44%
        """
        left, right = 0, len(numbers) - 1
        while left < right:  # Cannot do '<='. It can lead to 1 digit adding to itself.
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif (numbers[left] + numbers[right]) < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
# @lc code=end
