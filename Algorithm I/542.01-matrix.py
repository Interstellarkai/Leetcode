#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Simple Approach : BFS
        T : O(V^2 * MN) Exceed Time Limit
        S : O(B)
        """
        def bfs(mat: List[List[int]], i: int, j: int) -> int:
            m, n = len(mat), len(mat[0])
            import collections
            queue = collections.deque([(i, j)])
            visited = set([(i, j)])
            distance = 0
            while queue:
                level = len(queue)
                for i in range(level):
                    i, j = queue.popleft()
                    if mat[i][j] == 0:
                        return distance
                    directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                    for direction in directions:
                        x, y = direction
                        if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                            queue.append((x, y))
                            visited.add((x, y))
                distance += 1
        # Main
        m, n = len(mat), len(mat[0])
        res = [[None for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = bfs(mat, i, j)
        return res

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS on Zero's cell first
        T : O(mn) 76.34% | 775ms
        S : O(mn) 7.59% | 18.7mb
        """
        m, n = len(mat), len(mat[0])
        import collections  # imported by default already
        queue = collections.deque([])
        seen = set()
        res = [[float('inf')]*n for i in range(m)]

        # Find all Zeros
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    res[i][j] = 0
                    seen.add((i, j))

        # Expand from Zeros
        while queue:
            i, j = queue.popleft()
            # Expand outwards
            directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            for direction in directions:
                x, y = direction
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    res[x][y] = res[i][j] + 1
                    queue.append((x, y))
                    seen.add((x, y))

        return res

        # m, n = len(mat), len(mat[0])
        # DIR = [0, 1, 0, -1, 0]

        # q = deque([])
        # for r in range(m):
        #     for c in range(n):
        #         if mat[r][c] == 0:
        #             q.append((r, c))
        #         else:
        #             mat[r][c] = -1  # Marked as not processed yet!

        # while q:
        #     r, c = q.popleft()
        #     for i in range(4):
        #         nr, nc = r + DIR[i], c + DIR[i + 1]
        #         if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
        #         mat[nr][nc] = mat[r][c] + 1
        #         q.append((nr, nc))
        # return mat


def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    """
    Dynamic Programming
    From : https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
        1. In DP, we can only use previous values if they're already computed.
        2. In this problem, a cell has at most 4 neighbors that are left, top, right, bottom. If we use dynamic programming to compute the distance of the current cell based on 4 neighbors simultaneously, it's impossible because we are not sure if distance of neighboring cells is already computed or not.
        3. That's why, we need to compute the distance one by one:
            Firstly, for a cell, we restrict it to only 2 directions which are left and top. Then we iterate cells from top to bottom, and from left to right, we calculate the distance of a cell based on its left and top neighbors.
            Secondly, for a cell, we restrict it only have 2 directions which are right and bottom. Then we iterate cells from bottom to top, and from right to left, we update the distance of a cell based on its right and bottom neighbors.


    T : O(mn)
    S : O(mn)
    """
    m, n = len(mat), len(mat[0])

    for r in range(m):
        for c in range(n):
            if mat[r][c] > 0:
                top = mat[r - 1][c] if r > 0 else float('inf')
                left = mat[r][c - 1] if c > 0 else float('inf')
                mat[r][c] = min(top, left) + 1

    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if mat[r][c] > 0:
                bottom = mat[r + 1][c] if r < m - 1 else float('inf')
                right = mat[r][c + 1] if c < n - 1 else float('inf')
                mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

    return mat

# @lc code=end
