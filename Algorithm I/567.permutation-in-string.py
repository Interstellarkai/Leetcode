#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Simple Approach
        Problem: Time Limit Exceeded
        T : O()
        S : O()
        """
        from itertools import permutations
        for perm in permutations(s1):
            if ''.join(perm) in s2:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding Window (Github Co-pilot)
        T : O(N) 36.86% | 180ms
        S : O(1) 67.67% | 13.9mb
        """
        # Sanity Check
        if len(s1) > len(s2):
            return False
        # Initialize
        from collections import Counter
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])  # Window(2)
        # Basic Check
        if s1_counter == s2_counter:
            return True
        # Loop through the string (window)
        for i in range(len(s2) - len(s1)):  # How much more to slide
            # Shrink left window
            s2_counter[s2[i]] -= 1
            # House Keeping
            if s2_counter[s2[i]] == 0:
                del s2_counter[s2[i]]
            # Expand right window
                # i for concurrency between shrinking and expanding; len(s1) for window size
            s2_counter[s2[i + len(s1)]] += 1
            # Terminating Case
            if s1_counter == s2_counter:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Sliding Window
        T : O(N)
        S : O(1)
        """
        if len(s1) > len(s2):
            return False

        from collections import Counter
        counter = Counter(s1)

        for idx, ch in enumerate(s2):
            if ch in counter:
                counter[ch] -= 1

            # is the beginning letter inside the current sliding window
            left = idx - len(s1)
            if idx >= len(s1) and s2[left] in counter:
                counter[s2[left]] += 1

            # Alt: empty_counter = Counter()
            # Alt: if counter == empty_counter:
            if all([counter[i] == 0 for i in counter]):
                return True
        return False


# @lc code=end
