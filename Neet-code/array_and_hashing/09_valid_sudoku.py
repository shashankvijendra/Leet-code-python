# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

class Solution:
    def isValidSudoku(self, board) -> bool:
        
        for i in range(9):
            seen = set()
            for row in range(9):
                if board[i][row] == '.':
                    continue
                if board[i][row] in seen:
                    return False
                seen.add(board[i][row])
        
        
        for col in range(9):
            seen = set()
            for j in range(9):
                if board[j][col] == '.':
                    continue
                if board[j][col] in seen:
                    return False
                seen.add(board[j][col])
        
        for k in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = ((k//3)*3) + i 
                    col = ((k%3)*3) + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])   
        return True
    
    
# Input - 1:
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

# output : True

# Input: 
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

# Output: false

