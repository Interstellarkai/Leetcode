#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Recursion Method -> Time Limit Exceeded
        """
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs(self, n: int) -> int:
        """
        Top Down Approach -> Time Limit Exceeded
        """
        def topDown(n: int, storage: list) -> int:
            if n == 1 or n == 2:
                return n
            elif storage[n] != 0:
                return storage[n]
            else:
                storage[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            return storage[n]
        # Main
        # Initialize the memoization list
        storage = [0] * (n + 1)
        return topDown(n, storage)

    def climbStairs(self, n: int) -> int:
        """
        Bottom Up Approach
            Same as fibonacci sequence
        T : O() 6.12% | 66ms
        S : O() 56.9% | 13.9mb
        """
        if n == 1 or n == 2:
            return n

        twoStepAway = 1
        oneStepAway = 2
        for i in range(3, n + 1):
            currStep = twoStepAway + oneStepAway
            twoStepAway = oneStepAway
            oneStepAway = currStep
        return currStep

# @lc code=end
