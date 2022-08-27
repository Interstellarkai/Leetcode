#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Two pointers method. Inplace using python list insert and pop
        T : O(N) 96.11% | 36ms
        S : O(1) 85.62% | 13.8mb
        """
        i = j = 0
        # compare and do insertion
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                i += 1
                m += 1
                j += 1
            else:
                i += 1
        # Bring in the remaining num2
        while j < n:
            nums1.insert(m, nums2[j])
            nums1.pop()
            m += 1
            j += 1
        return nums1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Slicing method
        num[:] => pass by reference/pointer
        num => pass by value
        T : O(N) 32.51% | 66ms
        S : O(1) 85.62% | 13.9mb
        """
        i = j = 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1[:] = nums1[:i] + [nums2[j]] + nums1[i:-1]
                i += 1
                j += 1
                m += 1
            else:
                i += 1

        if j < n:
            nums1[:] = nums1[:m] + nums2[j:]
        return nums1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        T : O(N) 99.99%
        S : O(1)
        """
        while m > 0 and n > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n-=1
            else:
                nums1[m+n-1] = nums1[m-1]
                m-=1
        while n>0:
            nums1[m+n-1] = nums2[n-1]
            n-=1
# @lc code=end
