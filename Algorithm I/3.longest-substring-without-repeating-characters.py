#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    """
    Thought Process
    If asked for common strings then
        - Map (HashMap)
        - Trie
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Simple Approach with Map
        T : O(N^2) 11.78% | 650ms
        S : O(1) 49.10% | 14mb
        """
        if not s:
            return 0

        max_val = 1
        # Alt : seen = set()
        for left_ptr in range(len(s)):
            # Alt : seen.clear()
            right_ptr = left_ptr + 1
            temp_string = s[left_ptr]
            while right_ptr < len(s):
                # Alt : if s[right_ptr] in seen:
                if s[right_ptr] in temp_string:
                    break
                # Alt : seen.add(s[right_ptr])
                temp_string += s[right_ptr]
                right_ptr += 1
            max_val = max(max_val, right_ptr - left_ptr)
        return max_val

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window (Map)
        T : O(N) 95.77% | 58ms
        S : O(1) 49.26% | 14.1mb
        """
        # Intialized
        used = {}
        max_length = left = 0
        # Loop through the string (window)
        for right, ch in enumerate(s):
            # Basically left can't move left. It can only move right.
            # So either move it right or leave it unchanged.
            # e.g. Test Case "tmmzuxt"
            if ch in used and left <= used[ch]:
                left = used[ch] + 1
            else:
                max_length = max(max_length, right - left + 1)
            used[ch] = right
        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window (Github Co-Pilot)
        left = seen right + 1
        T : O(N) 62.95% | 88ms
        S : O(1) 49.26% | 14.1mb
        """
        if not s:
            return 0

        max_val = 1
        left = 0
        right = 0
        seen = set()
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                max_val = max(max_val, right - left + 1)
                right += 1
        return max_val
# @lc code=end
