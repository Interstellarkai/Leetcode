#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        """
        Same type of question to prefix calculator.
        T : O(N) 47.13% | 47ms
        S : O(N) 98.13% | 13.9mb
        """
        stack = []

        for char in s:
            if char == ']':
                substring = ''
                number = ''
                while stack and stack[-1] != '[':
                    substring += stack.pop()
                stack.pop()  # remove '['
                while stack and stack[-1].isdigit():
                    number += stack.pop()

                multiplier = int(number[::-1])

                stack.append(substring * multiplier)
            else:
                stack.append(char)

        # Reverse the string (as stack makes it reversed)
        for i in range(len(stack)):
            stack[i] = stack[i][::-1]

        return ''.join(stack)

    def decodeString(self, s: str) -> str:
        """
        Ref : https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
        When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
        push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
        the enclosed string k times.
        T : O(N)
        S : O(N)
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                # Just finished parsing this k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k for this new frame
                current_string = ""
                k = 0
            elif char == "]":
                # We have completed this frame, get the last current_string and k from when the frame
                # opened, which is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop(-1)
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char

        return current_string

    def decodeString(self, s: str) -> str:
        """
        Greedy Method.
        T : O(N) 99.99%
        S : O(N)
        Use recursion, make the locally optimal choice at each stage with the hope of finding a global optimal
        """
        result = ""
        index = 0
        while index < len(s):
            if s[index].isdigit():
                multiplier = int(s[index])

                while s[index+1].isdigit():
                    multiplier *= 10
                    multiplier += int(s[index+1])
                    index += 1

                # We may skip the opening bracket
                # since there is one and it adds no
                # additional information
                result += multiplier * self.decodeString(s[index+2:])
                index = self.getNextIndex(s, index+1)
            elif s[index] == "]":
                return result
            else:
                result += s[index]
                index += 1
        return result

    def getNextIndex(self, s, index):
        openings = 0
        while index < len(s):
            if s[index] == "[":
                openings += 1
            elif s[index] == "]":
                openings -= 1
                if openings == 0:
                    return index
            index += 1
        return index


# @lc code=end
