#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Using split() and join()
        T : O(N) 64.89% | 51ms
        S : O(N) 13.92% | 14.7mb
        """
        word = s.split(' ')
        for i in range(len(word)):
            word[i] = word[i][::-1]
        return ' '.join(word)
# @lc code=end
