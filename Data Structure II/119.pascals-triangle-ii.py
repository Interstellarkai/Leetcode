#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        T : O(N) 78.63% | 41ms
        S : O(N) 97.62% | 13.8mb
        """
        storage = [1]
        for _ in range(rowIndex):
            storage = [1] + [storage[i-1] + storage[i] for i in range(1, _)] + [1]
        return storage
# @lc code=end

