#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Brute force approach
        T : O(N^2)
        S : O(N)
        """
        # Hashtable for locating index location of num2
        dictionary = {}
        for index, val in enumerate(nums2):
            dictionary[val] = index

        result = []

        # check for each num1 ele
        for ele in nums1:
            index = dictionary[ele]
            # nums2; elements to the right
            right = nums2[index+1:]
            # temp holder for appending
            temp = None
            for val in right:
                if val > ele:
                    temp = val
                    break
            # append to result
            if temp:
                result.append(temp)
            else:
                result.append(-1)
        return result

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Stack approach
        Basically the problem says, if in nums1 we are working on 4, then in nums2 first find where is 4 and from that index find the next number greater than 4 in nums2. 
        We can see that the solution is always coming from the reverse side of the list nums2. This should tell us to use stack.

        Steps:
            1. We traverse nums2 and start storing elements on the top of stack.
            2. If current number is greater than the top of the stack, then we found a pair. Keep popping from stack till the top of stack is smaller than current number.
            3. After matching pairs are found, push current number on top of stack.
            4. Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, we can justify that next bigger element wasn't found for them. Hence we'll put -1 for the remaining elements in stack.

        T : O(N)
        S : O(N)
        """

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            # if stack is not empty, then compare it's last element with nums2[i]
            while stack and nums2[i] > stack[-1]:
                # if the new element is greater than stack's top element, then add this to dictionary
                mapping[stack[-1]] = nums2[i]
                # since we found a pair for the top element, remove it.
                stack.pop()
            # add the element nums2[i] to the stack because we need to find a number greater than this
            stack.append(nums2[i])

        # if there are elements in the stack for which we didn't find a greater number, map them to -1
        for element in stack:
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result


# @lc code=end
