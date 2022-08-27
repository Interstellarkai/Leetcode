#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Using DFS Recursion
        T : O(m*n) 98.68% | 279ms
        S : O(m*n) 49.19% | 16.5mb recursion calls
        """
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(grid, i, j):
            if (i < 0 or i >= m) or (j < 0 or j >= n) or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '~'
                return dfs(grid, i+1, j) or dfs(grid, i-1, j) or dfs(grid, i, j+1) or dfs(grid, i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)

        return count
# @lc code=end
