#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Recall: NTU's DSA Tutorial Qn
            RED | WHITE | BLUE
            Notice, Red is always left-end, Blue is always right-end
            Make use of pointer
        T : O(N) 39.85% | 67ms
            if you "blindly" swap after every selection, the count of swaps is N-1 and is constant;
            if you swap only when the selected element is not already in place, the count of swaps can be less (in the best case - a sorted array - the count is 0).
        S : O(1) 64.29% | 13.8mb
            since inplace
        """
        red = 0
        blue = len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red += 1
            elif nums[i] == 2:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -= 1
            # if nums[i] == 1, do nothing
            # Handle dirty exchange
            if red <= i and nums[i] != 1:
                continue
            i += 1

    def sortColors(self, nums: List[int]) -> None:
        """
        From Community Solution
        """
        red, white, blue = 0, 0, len(nums)-1
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

        

# @lc code=end

