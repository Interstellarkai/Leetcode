#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Use a dictionary to store the characters' occurences

        T : O(N)
        S : O(1)
        """
        from collections import Counter
        occurences = Counter(s)

        for index in range(len(s)):
            if occurences[s[index]] == 1:
                return index

        # Default
        return -1

    def firstUniqChar(self, s: str) -> int:
        """
        Same approach but without library

        T : O(N)
        S : O(1)
        """
        dictionary = {}
        for letter in s:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] += 1

        index = -1
        for i in range(len(s)):
            if dictionary[s[i]] == 1:
                index = i
                break

        return index
# @lc code=end
