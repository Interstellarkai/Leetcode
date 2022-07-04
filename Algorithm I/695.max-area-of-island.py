#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS with Stack
        T : O(mn) 32.10% | 421ms
        S : O(mn) 98.90% | 14mb
        """
        def dfs(grid: List[List[int]], i: int, j: int) -> int:
            m, n = len(grid), len(grid[0])
            max_area = 0
            stack = set()
            stack.add((i, j))
            while stack:
                # Main
                x, y = stack.pop()
                grid[x][y] = 0
                max_area += 1
                # Update the stack
                directions = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                for direction in directions:
                    i, j = direction
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        stack.add((i, j))
            return max_area

        largest = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counts = dfs(grid, i, j)
                    largest = max(largest, counts)

        return largest

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS with Recursion
        T : O(mn) 9.19% | 315ms
        S : O(mn) 5.31% | 18.7mb
        """
        def dfs(grid: List[List[int]], i: int, j: int) -> int:
            m, n = len(grid), len(grid[0])
            grid[i][j] = 0
            area = 1
            directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for direction in directions:
                x, y = direction
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    area += dfs(grid, x, y)
            return area

        largest = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    counts = dfs(grid, i, j)
                    largest = max(largest, counts)
        return largest

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        From Discussion, same approach, different implementation
        T : O(mn)
        S : O(mn)
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0
# @lc code=end
