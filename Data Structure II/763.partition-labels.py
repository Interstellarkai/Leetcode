#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#


# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        T : O(N) 23.12% | 57ms
        S : O(1) 23.78% | 16.2mb hashmap consist of max 26 keys
        """
        # Psuedocode
        # 1. Get all the first and last index of each elements
        # 2. Within each of these windows, the larger bracket will consumed the smaller one
        # 3. Return the last index of each of the finalized brackets

        # 1. Get all the first and last index of each elements
        window = {}
        for idx in range(len(s)):
            ch = s[idx]
            if ch not in window:
                window[ch] = (idx, idx)
            else:
                start, end = window[ch]
                window[ch] = (start, idx)

        # 2. Within each of these windows, the larger bracket will consumed the smaller one
        # Expected output: [0-8, 9-15, 16-23]
        res = []
        values = [value for value in window.values()]
        # print(values)
        prev_start, prev_end = values[0]

        for idx in range(1, len(values)):
            cur_start, cur_end = values[idx]

            # New bracket is a subset of Old bracket
            if prev_start < cur_start and cur_end < prev_end:
                continue

            # # Old bracket has spill over to New bracket
            elif prev_start < cur_start and prev_end < cur_end and cur_start < prev_end:
                prev_start, prev_end = prev_start, cur_end

            # New bracket is not a subset of Old bracket
            else:
                res.append((prev_start, prev_end))
                prev_start, prev_end = cur_start, cur_end

        if (prev_start, prev_end) not in res:
            res.append((prev_start, prev_end))
        # print(res)

        # 3. Return the last index of each of the finalized brackets
        return [y - x + 1 for x, y in res]

    def partitionLabels(self, s: str) -> List[int]:
        """
        https://leetcode.com/problems/partition-labels/solutions/1868757/python3-greedy-validation-explained/
        T : O(N) 96.88% | 36ms
        S : O(1) 98.78% | 13.8mb
        """
        L = len(s)
        last = {s[i]: i for i in range(L)}  # last appearance of the letter
        i, ans = 0, []
        while i < L:
            end, j = last[s[i]], i + 1
            while j < end:  # validation of the part [i, end]
                if last[s[j]] > end:
                    end = last[s[j]]  # extend the part
                j += 1

            ans.append(end - i + 1)
            i = end + 1

        return ans


# @lc code=end
