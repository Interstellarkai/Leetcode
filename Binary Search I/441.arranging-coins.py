#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start

class Solution:
    # https://leetcode.com/problems/arranging-coins/discuss/1559930/4-Java-Solution-with-Explanations%3A-Iterative-Binary-Search-Algebra-Math-and-Quadratic-Math
    def arrangeCoins(self, n: int) -> int:
        """
        Simple solution
        T : O(N^1/2) We take larger and larger chunks with each iteration
        S : O(1)
        """
        levels = 0
        while n > levels:
            levels += 1
            n -= levels
        return levels

    def arrangeCoins(self, n: int) -> int:
        """
        Concept: 
            Math Pattern
                1 + 2 + 3 + 4 .... + k = (1+k) * k / 2
                n = (k)(k + 1) /2
                n = (k + k **2) / 2
                k = (2n - k)^(1/2)
                return (int)((2 * n + 0.25)**0.5 - 0.5)
        Binary Search
        T : O(LogN)
        S : O(1)
        """
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            curSlots = mid * (mid + 1) // 2
            if curSlots <= n:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
# @lc code=end
