#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        If there is no missing number, then arr[i] should just be i+1.
        If there is a single missing number before arr[i], then arr[i] should be just i+2. So on so forth. 
        In general, if there are 'm' missing numbers up to aarr[i], arr[i] = i + m + 1. 
        So, when we see arr[i], we know there are arr[i]-i-1 missing numbers up to it. 
        If arr[i]-i-1 >= k or arr[i] > i+k, the k-th missing value must be between arr[i-1] and arr[i].


        On the other hand, if there have already been i numbers in arr, the k-th missing value must be at least k+i. 
        We show that k+i is actually the value we are looking for. 
            First, arr[i] > i+k, so i+k cannot be a[i]. 
            Neither can it be any arr[j], j > i, because arr is increasing and arr[j] > arr[i] > i+k. Can i+k appear before arr[i]? 
            If that is the case, say i+k = arr[j] for some j < i, then we will have arr[j] = i+k > j+k. 
        That means we would have found an earlier location j that triggers the arr[j] > j+k criterion, and we would have stopped over there.

        T : O(N) 45.49%
        T : O(1) 84.40%
        """
        for i, x in enumerate(arr):
            # [1] missing value is between arr[i-1] and arr[i] range
            if x > i + k:
                return i + k
        # [2] If nothing is missing
        return len(arr) + k

    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Note that in previous Solution all we cared about is the value arr[i]-i and if it is greater than k.
        Because arr is strictly increasing, arr[i]-i is also increasing! (arr[i+1] >= arr[i] + 1 => arr[i+1] - (i+1) >= arr[i] - i).
        Thus, we could use binary search over arr using arr[i]-i as the key for comparison.
        Unfortunately, the Python bisect*() does not support custom key. But no problem! We can write our own version of binary search.
        Binary Search
        T : O(LogN)
        S : O(1)
        """
        left = 1
        right = len(arr)
        while left <= right:
            mid = left + (right - left) // 2
            # There is missing val
            if arr[mid] > k + mid:
                right = mid
            else:
                left = mid + 1
        return right + k

# @lc code=end
