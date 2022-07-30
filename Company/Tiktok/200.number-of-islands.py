#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        T : O(mn) 91.47% | 315ms
        S : O(mn) 80.10% | 16.3mb recursive calls
        """
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                count += 1
        return count

    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            grid[i][j] = '0'
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)
        return

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    grid[i][j] == '0'
                    # self.bfs(grid, (i, j))
                    self.dfs(grid, (i, j))
                    count += 1
        return count

    def bfs(self, grid, start):
        nrows = len(grid)
        ncols = len(grid[0])
        r, c = start
        if grid[r][c] != '1':
            return

        import collections
        coords = collections.deque([start])
        grid[r][c] = '0'

        while coords:
            r, c = coords.popleft()
            if (r+1) < nrows and grid[r+1][c] == '1':
                coords.append((r+1, c))
                grid[r+1][c] = '0'
            if (r-1) >= 0 and grid[r-1][c] == '1':
                coords.append((r-1, c))
                grid[r-1][c] = '0'
            if (c+1) < ncols and grid[r][c+1] == '1':
                coords.append((r, c+1))
                grid[r][c+1] = '0'
            if (c-1) >= 0 and grid[r][c-1] == '1':
                coords.append((r, c-1))
                grid[r][c-1] = '0'

        return

    def dfs(self, grid, start):
        # Instead of recursion, we can go stack method.
        nrows = len(grid)
        ncols = len(grid[0])

        r, c = start
        if (r+1) < nrows and grid[r+1][c] == '1':
            grid[r+1][c] = '0'
            self.dfs(grid, (r+1, c))
        if (r-1) >= 0 and grid[r-1][c] == '1':
            grid[r-1][c] = '0'
            self.dfs(grid, (r-1, c))
        if (c+1) < ncols and grid[r][c+1] == '1':
            grid[r][c+1] = '0'
            self.dfs(grid, (r, c+1))
        if (c-1) >= 0 and grid[r][c-1] == '1':
            grid[r][c-1] = '0'
            self.dfs(grid, (r, c-1))

        return

# @lc code=end
