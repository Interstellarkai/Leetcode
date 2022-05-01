#
# @lc app=leetcode id=1385 lang=python3
#
# [1385] Find the Distance Value Between Two Arrays
#

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Brute Force Approach
        T : O(N^2)
        S : O(1)
        """
        answer = len(arr1)

        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    answer -= 1
                    break
        return answer

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        """
        Binary Search Approach
        T : O(NLogN)
        S : O(1)
        """

        arr2.sort()  # Ascending order
        answer = len(arr1)

        # Enumerate thru arr1
        for num in arr1:
            # Initialize for binary search
            low = 0
            high = len(arr2) - 1

            # Apply binary search to arr2 for speedy search in differences
            while (low <= high):
                # Main
                mid = low + (high - low)//2
                diff = abs(arr2[mid] - num)

                # Check for terminating condition
                if (diff <= d):
                    answer -= 1
                    break

                # Binary Search (Move Pointer to L)
                elif (num > arr2[mid]):
                    low = mid + 1  # To decrease the disparity

                # Binary Search (Move Pointer to R)
                else:
                    high = mid - 1  # To decrease the disparity
        return answer
# @lc code=end
