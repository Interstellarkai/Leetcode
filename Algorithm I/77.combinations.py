#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Using Library
            n : set(numbers)
            k : len(combination)
        T : O(n! * n) 99.95% | 66ms
        S : O(n!(n−r)! + n) 99.09% | 14.8mb
        """
        import itertools
        lst = [i for i in range(1, n+1)]
        return itertools.combinations(lst, k)  # O(n! * n)

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        https://leetcode.com/problems/combinations/discuss/844096/Backtracking-cheatsheet-%2B-simple-solution
        1. First level (IF), the function is implemented as recursion. At each occurrence of recursion, the function is one step further to the final solution.
        2. Second level (ELSE), within the recursion, we have an iteration that allows us to explore all the candidates that are of the same progress to the final solution.

        n = 4, k = 2
        []
        [1] -> [1, 2] -> [1, 3] ->[1, 4]
        [2] -> [2, 3] -> [2, 4]
        [3] -> [3, 4]
        [4]
        """
        result = []

        def backtrack(remain, combination, nex):
            # Base case
            if remain == 0:
                result.append(combination.copy())
            else:
                # Explore all possible candidates
                for i in range(nex, n+1):
                    # add candidate
                    combination.append(i)
                    # backtrack
                    backtrack(remain-1, combination, i+1)
                    # remove candidate
                    combination.pop()

        backtrack(remain=k, combination=[], nex=1)
        return result

    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        From GitHub Co-Pilot
        T : O(n! * n) 7.73% | 1004ms
        S : O(n!(n−r)! + n) 11.07% | 16.2mb
        """
        if k == 0:
            return [[]]
        if n == 0:
            return []
        return self.combine(n-1, k) + [i+[n] for i in self.combine(n-1, k-1)]


# @lc code=end
