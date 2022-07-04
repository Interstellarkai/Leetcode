#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Recursion
        https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
        T : O(2^N) Time Limit Exceeded
        S : O(2^N stack call)
        """
        def robWithIndex(nums: List[int], i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(robWithIndex(nums, i-2) + nums[i], robWithIndex(nums, i-1))

        return robWithIndex(nums, len(nums)-1)

    def rob(self, nums: List[int]) -> int:
        """
        Top Down with Memomization
        T : O(N) 60.77%  | 44ms
        S : O(N) 65.61%  | 13.8mb
        """
        def robWithIndex(nums: List[int], storage: List[int], i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            # Memomization
            if storage[i-2] == -1:
                storage[i-2] = robWithIndex(nums, storage, i-2)
            if storage[i-1] == -1:
                storage[i-1] = robWithIndex(nums, storage, i-1)
            # Main
            return max(storage[i-2] + nums[i], storage[i-1])

        storage = [-1] * (len(nums)+1)
        return robWithIndex(nums, storage, len(nums)-1)

    def rob(self, nums: List[int]) -> int:
        """
        Bottom Up with memoization
        T : O(N) 72.27% | 40ms
        S : O(N) 65.61% | 13.8mb
        """
        if len(nums) == 0:
            return 0
        storage = [None] * (len(nums)+1)
        storage[0] = 0
        storage[1] = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            storage[i+1] = max(storage[i], storage[i-1] + val)
        return storage[len(nums)]

    def rob(self, nums: List[int]) -> int:
        """
        Bottom Up without memoization
        T : O(N) 9.88% | 67ms
        S : O(1) 19.22% | 13.9mb
        """
        twoStepBehind = oneStepBehind = 0
        for i in range(len(nums)):
            currStep = max(twoStepBehind + nums[i], oneStepBehind)
            twoStepBehind = oneStepBehind
            oneStepBehind = currStep
        return currStep


# @lc code=end
