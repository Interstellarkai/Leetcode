#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        A function each for checking of row, col, and square of a Sudoku board
        T : O(N^2)
        S : O(N)
        """
        import collections

        def rowValid(board):
            # Booleans checked of each row
            valid = []
            for row in board:
                lst = [x for x in row if (x != '.')]
                valid.append(len(lst) == len(set(lst)))
            return all(valid)

        def colValid(board):
            # Booleans checked of each col
            valid = []
            for i in range(len(board)):
                col = []
                for j in range(len(board[0])):
                    if board[j][i] != '.':
                        col.append(board[j][i])
                valid.append(len(col) == len(set(col)))
            return all(valid)

        def squareValid(board):
            # Booleans checked of each col
            valid = []
            # 3 by 3 spacings
            for row in (0, 3, 6):
                for col in (0, 3, 6):
                    # containerize the 3 by 3 grid into a list
                    square = [board[x][y] for x in range(
                        row, row + 3) for y in range(col, col + 3) if board[x][y] != '.']
                    valid.append(len(square) == len(set(square)))
            return all(valid)

        # Main
        return rowValid(board) and colValid(board) and squareValid(board)

    def isValidSudoku(self, board):
        """
        How do you handle when c < 1 or c > 9?
            - Since c is a string, those comparisons aren't even defined.
        Can you explain tuple (i/3, j/3, c)? why not (i, j, c)?
            - Because (i/3, j/3) identifies one of the nine 3x3 blocks.
        why (val, colIndex) but (rowIndex, val)? (the order of val, colIndex, and rowIndex)
            - To distinguish rows and columns, for example ('4', 4) and (4, '4').

        T : O(N^2)
        S : O(N)
        """
        seen = []
        for rowIndex, row in enumerate(board):
            for colIndex, val in enumerate(row):
                if val != '.':
                    seen += [(val, colIndex), (rowIndex, val),
                             (rowIndex/3, colIndex/3, val)]
        return len(seen) == len(set(seen))

# Trial
# board = [["5","3",".",".","7","7",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]

# dictionary = {}
# from collections import Counter
# from pprint import pprint
# def isValidSudoku(board):
#     seen = []
#     for rowIndex, row in enumerate(board):
#         for colIndex, val in enumerate(row):
#             if val != '.':
#                 print([(val,colIndex),(rowIndex,val),(rowIndex/3,colIndex/3,val)])
#                 seen += [(val,colIndex),(rowIndex,val),(rowIndex/3,colIndex/3,val)]
#     dictionary = Counter(seen)
#     print(seen)
#     return dictionary

# pprint(isValidSudoku(board))

# @lc code=end
