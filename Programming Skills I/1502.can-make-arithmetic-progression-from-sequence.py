#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        T : O(NLogN)
        S : O(1)
        """
        arr.sort()
        difference = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) != difference:
                return False
        return True

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        T : O(N)
        S : O(N)
        """
        # gap 
        gap = (max(arr) - min(arr)) / (len(arr)-1)
        
        if gap == 0:
            return True

        for ele in arr:
            ele = ele - min(arr)
            if (ele % gap) != 0:
                return False

        return True
# @lc code=end
