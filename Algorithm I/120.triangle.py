#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Recursion
        T : O(N*N/2)
        S : O(N*N/2)
        """
        def minimumTotalByIndex(triangle: List[List[int]], i: int, j: int) -> int:
            # Sanity Check : Base of the triangle (Nothing more to call)
            if i == len(triangle) - 1:
                return triangle[i][j]
            # Main : Move to the next level
            left = minimumTotalByIndex(triangle, i + 1, j)
            right = minimumTotalByIndex(triangle, i + 1, j + 1)
            return triangle[i][j] + min(left, right)

        return minimumTotalByIndex(triangle, 0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        In-Place Top to Bottom
        From : https://leetcode.com/problems/triangle/discuss/1169431/Short-and-Simple-Solutions-w-Explanation-or-4-Lines-of-Code-w-Comments
        T : O(N^2) 25.25% | 128ms
        S : O(1) 59.65% | 14.9mb
        """
        # # Bottom to Top iteration
        # for level in range(1, len(triangle)):
        #     for i in range(level+1):
        #         triangle[level][i] += min(triangle[level-1][min(i, level-1)], triangle[level-1][max(i-1,0)])
        # return min(triangle[-1])

        # Top to Bottom iteration
        for level in range(len(triangle)-2, -1, -1): # 2nd Last row -> First row
            for i in range(level+1): # Recall : Row 0 : 1 Col, Row 1 : 2 Col
                triangle[level][i] += min(triangle[level+1][i], triangle[level+1][i+1])
        return triangle[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Top Down with Memoization
        T : O(N*N/2)
        S : O(2N)
        """
        def minimumTotalByIndex(triangle: List[List[int]], storage: List[List[int]], i: int, j: int) -> int:
            # Sanity Check : Base of the triangle (Nothing more to call)
            if i == len(triangle) - 1:
                return triangle[i][j]
            # Main : Move to the next level
            if not storage[i + 1][j]:
                storage[i + 1][j] = minimumTotalByIndex(triangle, storage, i + 1, j)
            if not storage[i + 1][j + 1]:
                storage[i + 1][j +1] = minimumTotalByIndex(triangle, storage, i + 1, j + 1)

            left, right = storage[i+1][j], storage[i+1][j+1]
            return triangle[i][j] + min(left, right)

        storage = [[None] * len(triangle[i]) for i in range(len(triangle))]
        return minimumTotalByIndex(triangle, storage, 0, 0)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Top Down with Auxillary Space
        From : https://leetcode.com/problems/triangle/discuss/1169431/Short-and-Simple-Solutions-w-Explanation-or-4-Lines-of-Code-w-Comments
        T : O(N^2)
        S : O(N)
        """
        n = len(triangle)
        # We can observe in the above solutions that we really ever access only two rows of the input at the same time.
        # So, we can just maintain two rows and alternate between those two in our loop.
        cur_row, next_row = [0]*n, triangle[n-1]
        for level in range(n-2, -1, -1):  # 2nd Last row -> First row
            for i in range(level+1):  # Recall : Row 0 : 1 Col, Row 1 : 2 Col
                cur_row[i] = triangle[level][i] + \
                    min(next_row[i], next_row[i+1])
            cur_row, next_row = next_row, cur_row
        return next_row[0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom Up with Auxillary Space
        From : https://leetcode.com/problems/triangle/discuss/1169431/Short-and-Simple-Solutions-w-Explanation-or-4-Lines-of-Code-w-Comments
        T : O(N^2) 26.23% | 127ms
        S : O(N) 92.34% | 14.9mb
        """
        n = len(triangle)
        # We can observe in the above solutions that we really ever access only two rows of the input at the same time.
        # So, we can just maintain two rows and alternate between those two in our loop.
        cur_row, prev_row = [0]*n, [0]*n
        prev_row[0] = triangle[0][0]
        for level in range(1, n):
            for i in range(level+1):
                cur_row[i] = triangle[level][i] + \
                    min(prev_row[min(i, level-1)], prev_row[max(i-1, 0)])
            cur_row, prev_row = prev_row, cur_row
        return min(prev_row)


# @lc code=end
