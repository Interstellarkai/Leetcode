#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Binary Search
        T : O(LogN)
        S : O(1)
        """

        low = 0
        high = len(letters) - 1

        # Sanity Check : Default case
        if target < letters[low] or target >= letters[high]:
            return letters[low]

        while low <= high:
            middle = (low + high) // 2
            candidate = letters[middle]

            if target < candidate:
                high = middle - 1

                # because we're looking for the smallest value that's greater than the target
                # we can condense the typical case where target == letters[middle] into the
                # the target > letters[middle] case
            if target >= candidate:
                low = middle + 1

        return letters[low]
# @lc code=end
