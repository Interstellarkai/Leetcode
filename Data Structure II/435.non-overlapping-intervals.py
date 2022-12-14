#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Sort by end time
        T : O(N Log N) 94.11% | 1397ms
        S : O(1) 90.20%% | 52.1mb
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                # Valid
                count += 1
                end = intervals[i][1]

        return len(intervals) - count

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Sort by end time
        T : O(N Log N) 87.97% | 1497ms
        S : O(1) 60.63%% | 52.8mb
        """
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        res = 0
        for i in range(1, len(intervals)):
            _, y1 = intervals[i-1]
            x2, _ = intervals[i]
            if not (y1 <= x2):
                res += 1
                # Remove an element by index from a list is O(N) time complexity; Whilst splicing will incur space complexity.
                # Hence, we remove the overlapping interval that has a larger end time (by swapping, O(1))
                intervals[i-1], intervals[i] = intervals[i], intervals[i-1]

        return res


# @lc code=end
