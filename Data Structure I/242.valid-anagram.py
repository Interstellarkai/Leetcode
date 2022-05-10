#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Similar to Leetcode 383
        T : O(N^2) => 43ms
        S : O(1)
        """
        if len(s) != len(t):
            return False

        for letter in set(s):
            if s.count(letter) > t.count(letter):
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Similar to Leetcode 383
        T : O(N) => 37ms
        S : O(N)
        """
        from collections import Counter
        occurenceS = Counter(s)
        occurenceT = Counter(t)
        return occurenceS == occurenceT

# @lc code=end
