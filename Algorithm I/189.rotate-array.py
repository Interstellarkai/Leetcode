#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Method 1
        nums[:] = list (by value, nums still the same address)
        nums = list (by address, nums will point to new address)

        T : O(N) 98.90% | 206ms
        S : O(N) 74.47% | 25.4mb
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Method 2
        T : O(NK) 5.95% | 3025 ms
        S : O(1) 27.32% | 25.5mb
        """
        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Method 3
        Idea:
        When the elements moved right by K times,
        the tail kmodn elements will rotate to the head, and the rest of the elements will move right by kmodn times.

        1. Reverse the whole array, in this casem the tail kmodn elements are now at the head
        2. Rotate the elements between [0,kmodn -1]
        3. Rotate the elements between [kmodn,n-1] 

        Example:
        nums = [1,2,3,4,5,6,7], n = 7 and k = 3,
        Original:                       [1,2,3,4,5,6,7]
        Reverse:                        [7,6,5,4,3,2,1]
        Rotate [0, kmodn -1] elements:  [5,6,7,4,3,2,1]
        Rotate [kmodn, n-1] elements:   [5,6,7,1,2,3,4]

        T : O(N) 90.67% | 223ms
        S : O(1) 74.47% | 25.4mb
        """
        def swap(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        length = len(nums)
        k %= length
        swap(nums, 0, length-k-1)
        swap(nums, length-k, length-1)
        swap(nums, 0, length-1)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Pythonic way of Method 3
        T : O(N)
        S : O(1)
        """
        length = len(nums)
        k %= length
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


# @lc code=end
