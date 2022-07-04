#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Using Library
        T : O(N!) 24.10% | 73ms
        S : O(N) 83.80% | 13.9mb
        """
        import itertools
        return list(itertools.permutations(nums))


class Solution:
    """
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res

    def backtracking(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                # Save
                visited.add(i)
                # Backtrack
                self.backtracking(res, visited, subset+[nums[i]], nums)
                # Remove
                visited.remove(i)
# @lc code=end
