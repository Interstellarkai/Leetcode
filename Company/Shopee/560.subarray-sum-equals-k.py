#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Array, HashTable
        E.g. When we are in index 4, we can only remove any of index 0~3.
        Bruteforce O(N^2) nested for loop.
        T : O(N)
        S : O(N)
        """
        # 1. Initialize the hash table (key (diff) : value (count of how many times it appears))
        # Why intialize 0:1? E.g., prefix is 1 and k is 1. The diff is 0. If we don't initalized this, we don't know how many times 0 appears.
        prefixSums = {0: 1}

        # 2. Initialize the curSum
        # curSum represents the curSum of subarray from index 0 to index i.
        curSum = 0

        # 3. Initialize the count
        count = 0

        # 4. Loop through the array
        for num in nums:
            # 5. Add the current number to the curSum
            curSum += num

            # 6. Check if there exist a diff in the hash table
            # Why? From this subarray, is there a number (diff) within it (excluding num[i]) that you can remove to get the intended k?
            diff = curSum - k

            # If diff in prefixSums, we add the count (number of ways to get this prefix into count). Else, just add 0
            count += prefixSums.get(diff, 0)

            # 8. Save the curSum to the hash table
            # Increment curSum if it is already in the hash table. Else, add it to the hash table with val as 0+1 = 1.
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        # 9. Return the count
        return count


# @lc code=end
