#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        T : O(N^2)
        S : O(1)
        """

        result = [[1]]

        for i in range(1, numRows):
            # Default start and end indexes have a val '1'
            result.append([1, 1])

            # Append previous sum of val into new list
            previousLst = result[i-1]
            if len(previousLst) > 1:
                for j in range(i-1):
                    sum = previousLst[j] + previousLst[j+1]
                    result[i].insert(j+1, sum)  # args: index, val
        return result

    def generate(self, numRows: int) -> List[List[int]]:
        """
        From Discussion
        """
        # Initialize a line structure
        l = [0]*numRows
        
        for i in range(numRows):
            # Initialize the triangle structure
            l[i] = [0]*(i+1)
            # Default start and end indexes have a val '1'
            l[i][0] = 1
            l[i][i] = 1
            
            # Generate sum of previous list
            for j in range(1, i):
                l[i][j] = l[i-1][j-1]+l[i-1][j]
        return l

# @lc code=end
