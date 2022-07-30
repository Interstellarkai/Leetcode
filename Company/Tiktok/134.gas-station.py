#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Greedy Approach
        Problem solving approach of making the locally optimal choice each stage with the hope of finding a global optimum.
        May not be the optimal solution, but it is fast.
        Whereas for dynamic programming, it is exhaustive and guaranteed to find the optimal solution
        T : O(N) 30.17% | 1137ms
        S : O(1) 68.17% | 19.2mb
        """
        # Sanity check
        if sum(gas) < sum(cost):
            return -1

        # Initialize
        start = 0
        tank = 0

        # There must be a solution since the the total tank after 1 cycle is greated than 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # Insufficient tank to complete the cycle, so we must start at the next possible location
            if tank < 0:
                start = i + 1
                tank = 0
        return start
# @lc code=end
