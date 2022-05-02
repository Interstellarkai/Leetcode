#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1. Make a Hash Table {val : index pos}
        2. Get the difference between each num to target
        3. If diff is not in the Hash Table, store difference
        4. Else, return the val (index)

        T : O(N)
        S : O(N)
        """
        # Initialize
        dictionary = {}

        for i in range(len(nums)):
            # Terminating Case
            if nums[i] in dictionary:
                return [dictionary[nums[i]], i]
            
            # Store difference in hash table
            else:
                difference = target - nums[i]
                dictionary[difference] = i


# @lc code=end
