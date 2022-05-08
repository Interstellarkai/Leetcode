#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Brute force approach:
        T : O(N^2)
        """
        lst = []
        for ele in nums2:
            if ele in nums1:
                lst.append(ele)
                nums1.remove(ele)
        return lst

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Counter approach:
        T : O(N)
        """
        import collections
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        c3 = c1 & c2 # & operator only works in set / dict
        return list(c3.elements())

        # lst = []
        # # Same key
        # for key in c1.keys() & c2.keys():
        #     # Expand the value
        #     lst.extend(key * min(c1[key], c2[key]))
        # return lst
# @lc code=end

