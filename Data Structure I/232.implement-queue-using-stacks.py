#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start

class MyQueue:
    """
    Python Queue implementation
    T : O(1) 94.46% | 28ms
    S : O(N) 21.85% | 14.1ms
    """

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        """Python FIFO queue enqueue"""
        self.queue.append(x)

    def pop(self) -> int:
        """Python FIFO queue dequeue"""
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def peek(self) -> int:
        """Python FIFO queue peek"""
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    def empty(self) -> bool:
        """Python FIFO queue check if queue is empty"""
        return True if len(self.queue) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
