
        
        
#Function that checks if the queens positioned in board are correctly placed
#board[i] = j means that there is a queen in the space (i,j)
def isValid(board):
    #We only check that the last queen is not threatend by any other
    lastQueenRow, lastQueenCol = len(board)-1, board[-1]
    
    #Check if the other queens threaten the last one
    for row, col in enumerate(board[:-1]):
        diffCol = abs(col- lastQueenCol)
        if (diffCol == 0) or (diffCol == lastQueenRow-row):
            return False
    
    return True


#Function that returns the amount of ways of positioning n queens correctly,
#where already some queens have been positioned in board
def nQueens(n, board=[]):
    #if the board is full, i.e. len(board)=n, there there is only one way
    if len(board) == n:
        return 1
    
    count = 0
    for col in range(n):
        board.append(col)
        if isValid(board):
            count += nQueens(n, board)
        board.pop()
        
    return count


class Solution:
    def totalNQueens(self, n: int) -> int:
        return nQueens(n, [])