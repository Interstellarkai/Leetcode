#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
from itertools import zip_longest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        T : O(n) 16.16% | 46 ms
        S : O(n) 6.5% | 16.3 mb
        """
        # Concept of bijection (Equal distinct counts, Equal no. of arrows)
        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s)))

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        T : O(n) 9.75% | 49 ms
        S : O(n) 6.5% | 16.4 mb
        """
        # Hash map
        s = s.split()

        if len(s) != len(pattern):
            return False
        if len(set(s)) != len(set(pattern)):
            return False

        hash_map_s = {}
        hash_map_pattern = {}

        for i, j in zip_longest(pattern, s):
            if i not in hash_map_s:
                hash_map_s[i] = j
            if j not in hash_map_pattern:
                hash_map_pattern[j] = i
            if hash_map_s[i] != j or hash_map_pattern[j] != i:
                return False

        return True


# @lc code=end
