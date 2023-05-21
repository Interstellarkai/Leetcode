#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time Limit Exceeded
            for loop: O(N)
                slicing : O(K)
                math.prod : O(N)
        """
        return [math.prod(nums[:idx] + nums[idx + 1 :]) for idx in range(len(nums))]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Two passes
        Compute product to the left and right of each element then combine these products to get the answer array
        T : O(N) 66.84% | 223 ms
        S : O(N) 25.56% | 22.4 mb
        """
        prefix_product = [1] * len(nums)
        postfix_product = [1] * len(nums)
        # Left to right
        for idx in range(1, len(nums)):
            prefix_product[idx] = prefix_product[idx - 1] * nums[idx - 1]
        # Right to left
        for idx in range(len(nums) - 2, -1, -1):
            postfix_product[idx] = postfix_product[idx + 1] * nums[idx + 1]
        # Result array
        return [prefix_product[idx] * postfix_product[idx] for idx in range(len(nums))]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Two passes
        Compute product to the left and right of each element then combine these products to get the answer array
        T : O(N) 40.37% | 244 ms
        S : O(1) 88.6% | 21.1 mb
        """
        answer = [1] * len(nums)
        prefix_product = 1
        postfix_product = 1
        # Left to right
        for idx in range(len(nums)):
            answer[idx] *= prefix_product
            prefix_product *= nums[idx]
        # Right to left
        for idx in range(len(nums) - 1, -1, -1):
            answer[idx] *= postfix_product
            postfix_product *= nums[idx]
        # Result array
        return answer


# @lc code=end
