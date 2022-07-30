#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        BackTracking Template
        T : O(N^2) 22.46% | 8861ms
        S : O(N^2) 92.85% | 13.8mb Recursion Call
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.backtracking(i, j, word, board):
                    return True
        return False

    def backtracking(self, i, j, word, board):
        # Terminating case
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False

        if board[i][j] == word[0]:
            # Save
            board[i][j] = "~"
            # Backtrack
            if self.backtracking(i+1, j, word[1:], board) or self.backtracking(i-1, j, word[1:], board) or self.backtracking(i, j+1, word[1:], board) or self.backtracking(i, j-1, word[1:], board):
                return True
            # Remove
            board[i][j] = word[0]
        return False

# @lc code=end
