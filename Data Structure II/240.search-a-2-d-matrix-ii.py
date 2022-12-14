#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Greedy method: start from top right (You don't want to start from lowest/highest val)
        T : O(N + M) 96.26% | 171ms
        S : O(1) 85.23% | 20.3mb
        https://leetcode.com/problems/search-a-2d-matrix-ii/solutions/2324351/python-explained/
        Consider the submatrix whose upper right corner is index i, j (row, column) and whose bottom left corner is the bottom left of the original matrix. (Bottom Left Quadrant)
        Suppose we know that the element we are searching for is either in this submatrix, or it is not in the matrix at all.
        If the target is greater than matrix[i][j] then we know the target is not in row i and we can now consider the submatrix whose upper right corner is i - 1, j.
        If the target is less than matrix[i][j] then we know that the target is not in column j and we can now consider the submatrix whose upper right corner is i, j-1.
        Initially we know that the element we are searching for is either in the matrix or it is not.
        In other words, we initially know that the element we are searching for is either in the submatrix whose upper right corner is at 0, m - 1 (where m is the number of columns) or it is not in the matrix at all.
        The idea of the algorithm is to maintain with each iteration the condition that the target is in the submatrix whose upper right corner is index i, j.


        Other Approach:
        1. Binary search on each row -> n log n
        2. Iterative Binary search to narrow search scope (Failed attempt: Example 1. Target = 26, depending on binary search implemetation)
        """
        if not matrix:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
# @lc code=end
