#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        T : O(N^2) 71.11% | 72ms
        S : O(N^2) 36.72% | 14mb
        """

        if n == 0:
            return []

        # 1. Initialize the matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        i, j = 0, 0
        di, dj = 0, 1  # For change of direction

        # 2. Walk the spiral path and write the numbers 1 to n*n
        for k in range(1, n * n + 1):  # O(N^2)
            matrix[i][j] = k

            # 3. Check if we can move to the next cell
            if matrix[(i + di) % n][(j + dj) % n] != 0:
                # 4. Make a right turn when the cell ahead is non-zero. (taken)
                # East  : 0,1
                # South : 1,0
                # West  : 0,-1
                # North : -1, 0
                di, dj = dj, -di
            # 5. Move to the next cell
            i += di
            j += dj
        return matrix
# @lc code=end
