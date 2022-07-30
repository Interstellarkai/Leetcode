#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Roman to Integer
        T : O(N)
        S : O(1)
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]
        return res

    def romanToInt(self, s: str) -> int:
        """
        Change
        T : O(N)
        S : O(1)
        """
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")  # 4, 9
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")  # 40, 90
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")  # 400, 900
        for char in s:
            number += translations[char]
        return number

# @lc code=end
