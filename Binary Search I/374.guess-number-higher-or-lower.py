#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Initialize
        min = 1
        max = n
        
        # Main
        while(min <= max):
            mid = int(min + (max-min)/2)
            g = guess(mid)

            # Terminating Case
            if (g == 0):
                return mid

            # Lower down my guess
            elif (g == -1):
                max = mid - 1
            else:
                min = mid + 1
        # Default : Error
        return -1
# @lc code=end

