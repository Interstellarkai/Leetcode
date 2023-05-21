#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        T : O(N) 6.84% | 48 ms
        S : O(1) 5.7% | 16.5 mb
        """
        # Base case
        if len(s) == 1:
            return 1

        # Palindrome (Even Even Even) or (Even Odd Even);
        # Even can be achieved with (odd - 1)
        counts = collections.Counter(s)
        answer = 0
        has_odd = False

        for count in counts.values():
            if count % 2 == 0:
                answer += count
            else:
                answer += count - 1
                has_odd = True

        if has_odd:
            answer += 1

        return answer


# @lc code=end
