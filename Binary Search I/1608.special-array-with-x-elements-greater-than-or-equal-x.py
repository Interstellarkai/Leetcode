#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Hint 1: Count the number of elements greater than or equal to x for each x in the range [0, nums.length].
        Hint 2: If for any x, the condition satisfies, return that x. Otherwise, there is no answer.
        T : O(N^2) 55.00%
        S : O(1) 14.59%
        """
        for i in range(len(nums) + 1):
            if sum(j >= i for j in nums) == i:
                return i
        return -1

    def specialArray(self, nums: List[int]) -> int:
        """
        Once you sort the nums array, exactly n-i numbers are greater than or equal the ith index number(num[i])
        So count takes a count = n-i of all those.
        If this count fulfills our question criteria written in if block, we return this as answer.
        If the entire array has been searched and no such number exists, we return -1.

        Without Binary Search 29ms, Using Linear Search. No nested for loop
        """
        nums.sort()
        n = len(nums)

        if n <= nums[0]:
            return n
        5, 3, 2, 1
        for i in range(1, n):
            count = n-i  # counts number of elements in nums greater than equal i
            if nums[i] >= (count) and (count) > nums[i-1]:
                return count
        return -1

    def specialArray(self, nums: List[int]) -> int:
        """
        Binary Search
        40 ms
        """
        nums.sort()
        n = len(nums)

        if n <= nums[0]:
            return n

        # binary search
        start, end = 0, n

        while(start <= end):
            mid = (start+end)//2
            # index of middle element
            count = 0
            for i in range(0, n):
                if nums[i] >= mid:
                    count = n-i
                    # count+=1 could use this but will take more iterations then.
                    break

            if count == mid:
                return count
            elif count < mid:
                end = mid-1
            else:
                start = mid+1

        return -1

# @lc code=end
