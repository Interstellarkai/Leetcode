#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    # Attempt 1: Mapping to list to enumerate
    def subtractProductAndSum(self, n: int) -> int:
        # Make into a str list to enumerate the digits
        n = str(n)
        
        # Initialize
        multiple = 1
        addition = 0
        
        for i in range(len(n)):
            digit = int(n[i]) # Typecast back to int
            multiple *= digit
            addition += digit
        return (multiple - addition)
        
    # Attempt 2: Remainder method to enumerate the digits
    def subtractProductAndSum(self, n: int) -> int:
        # Initialize
        addition = 0
        multiple = 1
        
        # enumerate through the num
        while(n > 0):
            # get the last digit
            digit = int(n % 10)
            
            addition += digit
            multiple *= digit
            
            # Shift new value to the ones place
            n = int(n/10)
        
        return (multiple - addition)
# @lc code=end

