#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Hash Table (Option 2)
        T : O(N) 32.61% | 246ms
        S : O(1) 84.34% | 16.6mb
        """
        from collections import Counter
        counter = Counter(nums)
        # Option 1 : NLogN from sorting
        # return counter.most_common()[-1][0]

        # Option 2 :
        # return min(counter, key=counter.get)

        # Option 3 :
        from operator import itemgetter
        min_key, min_count = min(counter.items(), key=itemgetter(1))
        return min_key

    def singleNumber(self, nums: List[int]) -> int:
        """
        Bit Manipulation
        T : O(N) 29.60% | 253ms
        S : O(1) 50.31% | 16.7mb
        """
        min_val = 0
        for num in nums:
            # XOR the same number with itself will be 0
            min_val ^= num
        return min_val


# @lc code=end
