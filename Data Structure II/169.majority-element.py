#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Hashmap (Option 3)
        T : O(N) 63.13% | 222ms
        S : O(1) 85.96% | 15.5mb
        """
        from collections import Counter
        counter = Counter(nums)
        # Option 1 : NLogN
        # return counter.most_common(1)[0] or counter.most_common()[0][0]

        # Option 2 : N
        # return max(counter, key=counter.get)

        # Option 3: N
        from operator import itemgetter
        return max(counter.items(), key=itemgetter(1))[0]

    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm
        From : Solution Approach 6
            If we had some way of counting instances of the majority element as +1+1+1 and instances of any other element as −1-1−1,
            summing them would make it obvious that the majority element is indeed the majority element.
        T : O(N)
        S : O(1)
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# @lc code=end
