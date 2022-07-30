#
# @lc app=leetcode id=1381 lang=python3
#
# [1381] Design a Stack With Increment Operation
#

# @lc code=start
class CustomStack:
    """
    T : O(N) 26.69% | 232ms
    S : O(N) 97.83% | 14.7mb
    """

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        for i in range(k):
            self.stack[i] += val


class CustomStack:
    """
    T : O(1)
    S : O(2N)
    """

    def __init__(self, maxSize: int):

        self.maxsize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:

        if len(self.stack) < self.maxsize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:

        if not self.stack:
            return -1

        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]

        return self.stack.pop()+self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc))-1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end
