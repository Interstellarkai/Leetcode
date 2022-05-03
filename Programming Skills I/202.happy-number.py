#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        With reference to solution.
        Learnt: A cycle is possible, so my appraoch to coding a terminating case for False is not feasible.
        T : O(LogN)
        S : O(LogN)
        """
        def looper(n: int) -> int:
            sum = 0
            while (n > 0):
                digit = n % 10  # Get the last digit
                n = n // 10  # Update N
                sum += digit**2
            return sum

        # For cycle checking
        checked = set()  # N.b. Set v.s. Dict
        while (n > 1):
            if n in checked:  # Seen -> a cycle
                return False
            else:
                checked.add(n)

            n = looper(n)

            if n == 1:  # Terminating case
                return True

    def isHappy(self, n: int) -> bool:
        """
        From the solution.
        Approach 2: Floyd's Cycle-Finding Algorithm
        T : O(LogN)
        S : O(1)

        Intuition
        The chain we get by repeatedly calling getNext(n) is an implicit LinkedList. 
        Implicit means we don't have actual LinkedNode's and pointers,
        but the data does still form a LinkedList structure. 
        The starting number is the head "node" of the list,
        and all the other numbers in the chain are nodes.
        The next pointer is obtained with our getNext(n) function above.

        Recognizing that we actually have a LinkedList, 
        This algorithm is based on 2 runners running around a circular race track, 
        a fast runner and a slow runner.

        Regardless of where the tortoise and hare start in the cycle,
        they are guaranteed to eventually meet. 
        This is because the hare moves one node closer to the tortoise (in their direction of movement) each step.
        """
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

# @lc code=end
