#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        Simple Approach to Matrix
        T : O(N^2)
        S : O(N)
        """
        # Sanity check for legality
        if (len(mat) * len(mat[0])) != (r*c):
            return mat
        
        # Flatten mat
        single_mat =[]
        for lst in mat:
            single_mat.extend(lst)

        # Main: restructure
        result = list()
        for i in range(r):
            # Dynamically add in a list
            result.append(list())
            for j in range(c):
                result[i].append(single_mat[0])
                single_mat.pop(0)

        # Another way to write the main restructure
        # for i in range(0,len(single_mat),c):
        #     result.append(single_mat[i:i+c])
        return result


# @lc code=end

