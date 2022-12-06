#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        DEQUE method
        T : O(N Log N) 10.36% | 418ms
        S : O(N) 54.21% |18.1mb
        """
        from collections import deque
        intervals.sort(key=lambda x: x[0])
        intervals = deque(intervals)
        res = []

        # main
        while intervals:
            if len(intervals) == 1:
                res.append(intervals.pop())
                continue
            node1 = intervals.popleft()
            node2 = intervals.popleft()
            leftend, rightend = max(node1[0], node2[0]), min(node1[1], node2[1])
            # Condition: overlap
            if leftend <= rightend:
                mergeNode = [min(node1[0], node2[0]), max(node1[1], node2[1])]
                intervals.appendleft(mergeNode)
            else:
                res.append(node1)
                intervals.appendleft(node2)

        return res

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Direct approach
        T : O(N Log N) 45.38% | 347ms
        S : O(1) 85.81% | 18.1mb
        """
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            # Condition: overlap
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            else:
                i += 1
        return intervals

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Stack method
        T : O(N log N) 27.34% | 382ms
        S : O(N) 85.81% | 18.1mb
        """
        intervals.sort(key=lambda x: x[0])
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if interval[0] <= stack[-1][1]:
                    stack[-1][1] = max(interval[1], stack[-1][1])
                else:
                    stack.append(interval)
        return stack


# @lc code=end

