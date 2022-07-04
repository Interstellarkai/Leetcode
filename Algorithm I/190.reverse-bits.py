#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Bit-wise Manipulation
        The code below does the following:
            1. Initialize the result to 0.
            2. For each bit in the binary representation of n, starting from the least significant bit,
                do the following:
                    a. Shift the result right by 1.
                    b. If the least significant bit of the result is 1, add 1 to the result.
                    c. Shift the n right by 1.
                    d. Repeat steps 2 through 4 until all bits in n have been processed.
            3. Return the result.
        T : O(1) 14.09% | 66ms
        S : O(1) 49.26% | 13.8mb
        """
        res = 0
        for i in range(32):
            # LSB = (n & 1)
            # Shift bits to the right by 'i' : << n
            res += (n & 1) << (31 - i)
            n >>= 1
        return res
# @lc code=end
