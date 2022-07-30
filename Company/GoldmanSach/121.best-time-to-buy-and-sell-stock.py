#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Simple Approach
        T : O(N^2) Exceed Time Limit
        S : O(1) Exceed Time Limit
        """
        res = 0
        for i in range(len(prices)-1):
            highest = max(prices[i+1:])  # T(N) operation
            if highest > prices[i]:
                curr = highest - prices[i]
                res = max(res, curr)
        return res

    def maxProfit(self, prices: List[int]) -> int:
        """
        Dynamic programming approach: Kadane's approach
        T: O(N) 52.38% | 1535ms
        S: O(1) 37.97% | 25mb
        """
        # Initialize
        maxProfit = 0
        minPurchase = prices[0]

        # Dynamic approach: iteration
        for i in range(1, len(prices)):
            currProfit = prices[i] - minPurchase
            maxProfit = max(maxProfit, currProfit)
            minPurchase = min(minPurchase, prices[i])

        return maxProfit
# @lc code=end
