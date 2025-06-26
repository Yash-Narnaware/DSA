#Leetcode - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def can_place(board, i, j):

            #check row
            for ii in range(i):
                if board[ii][j] == 'Q':
                    return False
        
            #check column
            for ii in range(j):
                if board[i][ii] == 'Q':
                    return False

            #check left diag
            i1, j1 = i - 1, j - 1
            while i1 >= 0 and j1 >= 0:
                if board[i1][j1] == 'Q':
                    return False
                i1 -= 1
                j1 -= 1

            #check right diag
            i1, j1 = i - 1, j + 1
            while i1 >= 0 and j1 < n:
                if board[i1][j1] == 'Q':
                    return False
                i1 -= 1
                j1 += 1

            return True

        
        def func(board,row,res):

            if row == n:
                res.append(board[:])
                return

            
            for j in range(n):
                if can_place(board, row, j):
                    board[row] = board[row][:j] + 'Q' + board[row][j+1:]

                    func(board, row+1, res)

                    board[row] = board[row][:j] + '.' + board[row][j+1:]

        board = ['.'*n for _ in range(n)]
        res = []
        func(board, 0, res)

        return res
        
