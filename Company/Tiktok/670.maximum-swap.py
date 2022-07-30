#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
from pyparsing import nums


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        T : O(N) 9.80% | 63ms
        S : O(1) 98.68% | 13.8mb
        Greedy Approach
            1. Find the start index of an increasing subsequence. (Because from left to right, what we want is decreasing order)
            2. On the right side of i (i.e. arr[i+1:]), find the max value (max_val) and its index (max_idx)
            3. On the left side of i (i.e. arr[:i]), find the most left value and its index (left_idx), which is less than max_val
            4. Swap above left_idx and max_idx if necessary
        """
        s = list(str(num))
        n = len(s)
        # find index where s[i] < s[i+1], meaning a chance to flip
        for i in range(n-1):
            if s[i] < s[i+1]:
                break
        else:
            # if nothing found, return num
            return num

        # keep going right, find the maximum value index
        max_idx, max_val = i+1, s[i+1]
        for j in range(i+1, n):
            if max_val <= s[j]:  # N.b. equal sign. RHS val has lower value than LHS val
                max_idx, max_val = j, s[j]

        # going right from i, find most left value that is less than max_val
        left_idx = i
        for j in range(i, -1, -1):
            if s[j] < max_val:
                left_idx = j

        # swap maximum after i and most left less than max
        s[max_idx], s[left_idx] = s[left_idx], s[max_idx]

        # re-create the integer
        return int(''.join(s))

    def maximumSwap(self, num: int) -> int:
        """
        T : O() 99.99%
        T : O()
        """
        high_digit = high_pos = 0
        low_digit = low_pos = 0
        cur_high_digit, cur_high_pos = -1, 0
        pos = 1
        res = num

        while num:
            digit = num % 10

            if digit > cur_high_digit:
                cur_high_digit, cur_high_pos = digit, pos

            elif digit < cur_high_digit:
                high_digit, high_pos = cur_high_digit, cur_high_pos
                low_digit, low_pos = digit, pos

            pos *= 10
            num //= 10

        res += high_digit*(low_pos - high_pos) + low_digit*(high_pos - low_pos)
        return res


# @lc code=end
