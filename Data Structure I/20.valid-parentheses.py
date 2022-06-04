#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        '(', ')', '{', '}', '[' and ']'
        Stack
        T : O(N) 33.92% | 50ms
        S : O(N) 69.47% | 13.9mb
        """
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                else:
                    return False
        return True if len(stack) != 0 else False

    def isValid(self, s: str) -> bool:
        """
        T : O(N) 19.71% | 57ms
        S : O(N) 23.68% | 13.9mb
        """
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if char == ')' and stack[-1] != '(':
                        return False
                    elif char == ']' and stack[-1] != '[':
                        return False
                    elif char == '}' and stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
        if len(stack) > 0:
            return False
        else:
            return True

# @lc code=end
