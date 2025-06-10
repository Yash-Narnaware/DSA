class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        def can_place(board,i,j):


            #check column
            for k in range(i):
                if board[k][j] == 'Q':
                    return False

            #check left diag
            i2 = i-1
            j2 = j-1
            while i2 >= 0 and j2 >= 0:
                if board[i2][j2] == 'Q':
                    return False
                i2 -= 1
                j2 -= 1

            #check right diag
            i2 = i-1
            j2 = j+1
            while i2 >= 0 and j2 < n:
                if board[i2][j2] == 'Q':
                    return False
                i2 -= 1
                j2 += 1

            return True
        
        def snq(board,i,res):

            if i == n:
                res.append(board.copy())
                return

            #check in each column
            for j in range(n):

                if can_place(board,i,j):
                    # board[i][j] = 'Q'
                    board[i] = board[i][:j] + 'Q' + board[i][j+1:] 

                    snq(board,i+1,res)

                # board[i][j] = '.'
                board[i] = board[i][:j] + '.' + board[i][j+1:] 



        board = ['.'*n for _ in range(n)]
        res = []

        snq(board,0,res)

        return res
        
