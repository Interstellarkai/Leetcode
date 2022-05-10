#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        T : O(N^2)
        S : O(N)
        """
        from collections import Counter
        occurenceR = Counter(ransomNote)
        occurenceM = Counter(magazine)

        for key in list(occurenceR.keys()):
            # check if they have the same letters
            if key in list(occurenceM.keys()):
                # check if there are enough same letter
                if occurenceM[key] < occurenceR[key]:
                    return False
            else:
                return False

        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Found from discussion
        T : O(N^2)
        S : O(1)
        """
        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True

# @lc code=end
