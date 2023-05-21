#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

import collections

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Idea: With reference to two-sum
        N.b., Subarray must be a contiguous (Adjacent elements)

            to count all subarrays sum up to k
            
            we can count all possible sums iterating through nums
            and use
            
                sum[i:j] = sum[:j] - sum[:i]
            
            to check if sum[i:j] == k, and with the count of sums before j
            we can add count[sum[:j] - k] to the final count at each j
            
            we will want to initiate count[0] to 1, so that sum[:j] == k can be counted

        T : O(N) 72.54% | 297 ms
        S : O(N) 97.17% | 16.5 mb
        """
        answer = 0
        # keep track of the sum of elements seen so far. To easily compute the sum of any subarray by taking the difference between two running sums.
        curr_sum = 0
        sum_counts = collections.defaultdict(int)
        
        sum_counts[0] = 1 # Initialize with {0:1} to handle the case when curr_sum == k
        
        for num in nums:
            curr_sum += num # sum[:j]
            diff = curr_sum - k # sum[:i] = sum[:j] - sum[i:j]

            # check if the difference diff between curr_sum and k is in the dictionary sum_counts
            if diff in sum_counts: # Is there a sum[:i] ?
                answer += sum_counts[diff]

            # update the dictionary sum_counts to include the current sum curr_sum. 
            sum_counts[curr_sum] += 1
            
        return answer



# @lc code=end
