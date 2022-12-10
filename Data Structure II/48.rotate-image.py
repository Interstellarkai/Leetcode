#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Idea:
        Ultimate goal:              M(r, c) ---> M'(c, N-1-r)
        1. Transpose the matrix     M(r, c) ---> M'(c, r)
        2. Reverse each row         M(r, c) ---> M'(c, N-1-r)
        T : O(N^2) 57.96% | 65ms
        S : O(1) 30.30% | 13.9mb
        """
        # Initialize
        N = len(matrix)

        # Transpose
        for r in range(N):
            for c in range(r, N):
                # Only act on upper triangle or lower triangle to achieve this goal
                if c > r:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Flip in each row
        for r in range(N):
            for c in range(N//2):
                matrix[r][c], matrix[r][N-1-c] = matrix[r][N-1-c], matrix[r][c]

        """
        for r in range(N):
            r[:] = r[::-1]

        Run the following code to know if you're doing list in-place or not
        # print hex(id(x))
        id(list)
        list[:] = list[len(list) - k:] + list[:len(list) - k]
        id(list)  # prints the same id as above

        id(list)
        list = list[len(list) - k:] + list[:len(list) - k]
        id(list)  # prints a new id representing a new list object
        """
# @lc code=end
