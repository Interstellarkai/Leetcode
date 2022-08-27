#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        """
        Greedy Approach
        Problem solving approach of making the locally optimal choice each stage with the hope of finding a global optimum.
        May not be the optimal solution, but it is fast.
        Whereas for dynamic programming, it is exhaustive and guaranteed to find the optimal solution

        Greedy Approach
            1. If we try to tranverse the digits from left to right, there are many different cases we need to consider. 
            2. But if we tranverse the digits from right to left, it is very straightforward! 
            3. Whenever a digit is smaller than a digit to its left, decrease its left digit by 1 and convert all the digits from here until the end to 9.
            4. To make the digits easy to access, tranverse, and modify, I converted the number into a list of integers.

        T : O(N) 9.95% | 66ms
        S : O(1) 64.36% | 13.8mb
        """
        # Base case
        if n == 0:
            return 0
        if n < 10:
            return n

        # Convert number to list of integers
        lst = [int(i) for i in str(n)]

        # 11.60% | 65ms
        # 20.17% | 14mb
        # cache_ptr = len(lst)
        # # Transverse from right to left
        # for i in range(len(lst)-1, 0, -1):
        #     # Trigger condition
        #     if lst[i-1] > lst[i]:
        #         # LHS decreases by 1
        #         lst[i-1] -= 1
        #         # RHS all set to 9
        #         for j in range(i, cache_ptr):
        #             lst[j] = 9
        #         # update cache to prevent
        #         cache_ptr = i

        # return int("".join([str(x) for x in lst]))

        last = len(lst)
        # Tranverse from right to left
        for i in range(len(lst)-1, 0, -1):
            # Trigger
            if lst[i-1] > lst[i]:
                lst[i-1] -= 1
                last = i

        # Update all other digits to 9
        for i in range(last, len(lst)):
            lst[i] = 9
        return int("".join([str(x) for x in lst]))


# @lc code=end
