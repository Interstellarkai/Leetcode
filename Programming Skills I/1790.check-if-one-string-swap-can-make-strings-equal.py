#
# @lc app=leetcode id=1790 lang=python3
#
# [1790] Check if One String Swap Can Make Strings Equal
#

# @lc code=start
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Simple Brute Force Approach
        T : O(N)
        S : O(N)
        """
        def compare(s1: str, s2: str) -> list:
            compare = []
            falseCounts = 0
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    compare.append(True)
                else:
                    compare.append(False)
                    falseCounts += 1
            return compare, falseCounts

        # Main
        compare, falseCounts = compare(s1, s2)
        if falseCounts == 0:
            return True

        # Attempt to change (Works if there's only 2 index to change)
        location = [x for x, y in enumerate(compare) if y == False]
        if len(location) != 2:
            return False

        # Python does not support string assignment
        s2 = list(s2)
        # Swap
        temp = s2[location[0]]
        s2[location[0]] = s2[location[1]]
        s2[location[1]] = temp
        # Python does not support string assignment
        s2 = "".join(s2)

        # Check
        return s1 == s2

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        From Discussion
        T : O(NLogN)
        """
        c = 0
        for i, j in zip(s1, s2):
            if i != j:
                c += 1
        return s1 == s2 or (sorted(s1) == sorted(s2) and c == 2)

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        From Discussion
        T : O(N)
        """
        from collections import Counter
        count = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                count += 1
        # counter(): a list of counts based on elements occurences
        return (Counter(s1) == Counter(s2)) and (count == 0 or count == 2)

# @lc code=end
