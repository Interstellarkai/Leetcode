#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Dynamic programming approach: RunTime Error
        T: O(N)
        S: O(1)
        """
        # Initialize
        maxVal = 0
        for i in range(len(prices) - 1):
            curVal = max(prices[i+1:]) - prices[i]
            maxVal = max(curVal, maxVal)
        return maxVal

    def maxProfit(self, prices: List[int]) -> int:
        """
        Taken from discussion
        """

        maxProfit = 0
        minPurchase = prices[0]
        
        for i in range(1, len(prices)):		
            maxProfit = max(maxProfit, prices[i] - minPurchase)
            minPurchase = min(minPurchase, prices[i])
        return maxProfit
# @lc code=end
