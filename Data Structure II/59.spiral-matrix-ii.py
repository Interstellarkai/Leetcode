#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        T : O(N^2) 20.91% | 69ms
        S : O(N^2) 39.76% | 14mb
        """
        # Turn right when the next position is out of bound or already visited
        # 0: right, 1: down, 2: left, 3: up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Create the matrix
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        # Initialize the position and direction
        idx = 0
        pos = (0, 0)

        # Main loop
        for num in range(1, n * n + 1):
            i, j = pos
            print(pos)
            matrix[i][j] = num
            next_i, next_j= i + directions[idx][0], j + directions[idx][1]
            # Change direction if corner or taken
            if (next_i < 0) or (next_i >= n) or (next_j < 0) or (next_j >= n) or matrix[next_i][next_j] != 0:
                idx = (idx + 1) % 4
            # Default: move forward
            pos =  (i + directions[idx][0], j + directions[idx][1])
        return matrix
# @lc code=end

