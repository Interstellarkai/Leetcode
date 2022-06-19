#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
        """
        Do not return anything, modify s in-place instead.
        """
    def reverseString(self, s: List[str]) -> None:
        """
        Built-in
        T : O(N) 72.39% | 223ms
        S : O(1) 46.40% | 18.5mb
        """
        s.reverse()
        # Accessing Elements in Reversed Order
        # If you need to access individual elements of a list in the reverse order,
        # it's better to use the reversed() function.
        # s = reversed(s)

    def reverseString(self, s: List[str]) -> None:
        """
        Slicing Operator
        T : O(N) 34.55% | 309ms
        S : O(1) 15.66% | 18.7mb
        """
        s[:] = s[::-1] # by value, same address

    def reverseString(self, s: List[str]) -> None:
        """
        Two Pointers
        T : O(N/2) 94.11% | 202ms
        S : O(1) 87.26% | 18.4mb
        """
        left, right = 0, len(s)-1
        while left < right: # should not do <=
            s[left], s[right] = s[right], s[left]
            left += 1
            right += 1


# @lc code=end

