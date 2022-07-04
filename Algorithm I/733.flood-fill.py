#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Simple Approach
        T : O(V^2) 5.18% | 171ms
            Adjacency List -> O(V + E)
            Adjacency Matrix -> O(V^2)
        S : O(N) 65.46% | 14mb
        """
        # Initialize
        queue = [(sr, sc)]
        original_color = image[sr][sc]
        m = len(image)
        n = len(image[0])
        # Sanity check
        if original_color == color:
            return image
        # Main
        while queue:
            sr, sc = queue.pop(0)
            if 0 <= sr < m and 0 <= sc < n:
                if image[sr][sc] == original_color:
                    image[sr][sc] = color  # change color
                    queue.append((sr-1, sc))  # up
                    queue.append((sr+1, sc))  # down
                    queue.append((sr, sc-1))  # left
                    queue.append((sr, sc+1))  # right
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Improved with library
        T : O(V^2) 21.12% | 139ms
            Adjacency List -> O(V + E)
            Adjacency Matrix -> O(V^2)
        S : O(N) 89.69% | 14mb
        """
        import collections
        original_color, m, n = image[sr][sc], len(image), len(image[0])
        if original_color != color:
            queue = collections.deque([(sr, sc)])  # Doubly-Linked-List
            while queue:
                i, j = queue.popleft()  # O(1) instead of O(N) from pop(0)
                # Change Color
                image[i][j] = color

                # Up, Down, Left, Right
                directions = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                for x, y in directions:
                    if 0 <= x < m and 0 <= y < n and image[x][y] == original_color:
                        queue.append((x, y))
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        From LeetCode submission
        T : O(V^2) 99.99%
        S : O(N)
        """
        R, C = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def dfs(r, c):
            if image[r][c] == original_color:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1, c)
                if r+1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c+1 < C:
                    dfs(r, c+1)

        dfs(sr, sc)
        return image
# @lc code=end
