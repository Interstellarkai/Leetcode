#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Idea : Merge the list, do binary search
        T : O(LogN)
        S : O(N)
        """
        # Convert the matrix into a list
        concatenated = []
        for ele in matrix:
            concatenated.extend(ele)

        # Binary search
        left = 0
        right = len(concatenated) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if concatenated[mid] == target:
                return True
            elif concatenated[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
# @lc code=end
