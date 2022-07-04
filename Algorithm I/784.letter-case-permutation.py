#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Backtracking
        T : O(m+n) 5.01% | 1303ms
        S : O(1) 20.44% | 15.4mb
        """
        res = []

        def backtrack(permutation, s, length):
            if len(permutation) == length:
                res.append(permutation)
            else:
                for i in range(len(s)):
                    if s[i].isalpha():
                        backtrack(permutation + s[i].upper(), s[i+1:], length)
                        backtrack(permutation + s[i].lower(), s[i+1:], length)
                    else:
                        backtrack(permutation + s[i], s[i+1:], length)

        backtrack(permutation="", s=s, length=len(s))
        return res

    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Backtracking
        From : https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution
        T : O(m+n)
        S : O(1)
        """
        def backtrack(substring="", i=0):
            if len(substring) == len(s):
                res.append(substring)
            else:
                if s[i].isalpha():
                    backtrack(substring + s[i].swapcase(), i + 1)
                backtrack(substring + s[i], i + 1)

                # To trigger a recursion without swapcase for alpha, and for not alpha
                # if s[i].isalpha():
                #     backtrack(substring + s[i].swapcase(), i + 1)
                #     backtrack(substring + s[i], i + 1)
                # else:
                #     backtrack(substring + s[i], i + 1)
        res = []
        backtrack()
        return res
# @lc code=end
