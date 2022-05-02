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
        Brute Force Approach (Merge, Sort all)
        T : O(NLogN)
        S: (1)
        """
        # Make them as one list
        for i in range(n):
            nums1[m+i] = nums2[i]
        # Library sort
        nums1.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Brute Force Approach (Merge, Sort new elements)
        T : O(N^2)
        S: (1)
        """
        # Make them as one list
        for i in range(n):
            nums1[m+i] = nums2[i]
        # Insertion Sort on newly added elements
        for i in range(n):
            pointer = m + i
            while (pointer >= 1):
                if (nums1[pointer] < nums1[pointer - 1]):
                    # Swap
                    temp = nums1[pointer - 1]
                    nums1[pointer - 1] = nums1[pointer]
                    nums1[pointer] = temp
                    # Repeat
                    pointer -= 1
                else:
                    break

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Brute Force Approach (Insert in order)
        T : O(NLogN)
        S: (1)
        """
        # Ignore all the zeros
        del nums1[m:]

        # Pointers
        nums1Ptr = nums2Ptr = 0
        
        # Merge sort concept 
        while ((nums1Ptr < len(nums1)) and (nums2Ptr < n)):
            # Trigger to do insertion
            if nums1[nums1Ptr] > nums2[nums2Ptr]:
                nums1.insert(nums1Ptr, nums2[nums2Ptr])
                nums2Ptr += 1
            # Default increment
            nums1Ptr += 1

        # not all nums2 are added into nums1
        while (nums2Ptr < n):
            nums1.insert(nums1Ptr, nums2[nums2Ptr])
            nums1Ptr += 1
            nums2Ptr += 1


# @lc code=end
