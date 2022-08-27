#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        T : O(M*N) 76.76% | 44ms
        S : O(N) 88.78% | 13.9mb
        """
        n = len(strs)
        # shortestWord  = sorted(strs, key=len)[0]
        shortestWord =  min(strs, key=len)
        
        # Testcase [""] => [""]
        if not shortestWord:
            return shortestWord
        
        res = []

        for i in range(len(shortestWord)):
            for j in range(len(strs)):
                if strs[j][i] != shortestWord[i]:
                    return ''.join(res)
            res.append(shortestWord[i])
            
        # Testcase ["a"] => "a"
        return ''.join(res)
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        T : O(M*N) 48.18% | 56ms
        S : O(N) 50.32% | 13.9mb
        """
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            # returns the index of found char, else -1
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1] # Go to next char
                if not prefix:
                    return ""
        return prefix
# @lc code=end

