#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Mapper to implicitly convert str to int
        T : O(N) 13.76% | 53 ms
        S : O(1) 75.62% | 13.9 mb
        """

        def stringToNum(num):
            mapper = {
                "0": 0,
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
            }
            number = 0
            for idx in range(len(num)):
                number *= 10
                number = mapper[num[idx]]

        return stringToNum(num1) + stringToNum(num2)


# @lc code=end
