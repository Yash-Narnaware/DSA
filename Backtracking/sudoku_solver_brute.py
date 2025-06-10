#brute force sudoku solver code. will give TLE on leetcode #37

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        #helper function to check if we can put particular number on given cell
        def can_place(board,i,j,k):


            #check row:
            for m in range(9):
                if board[i][m] == str(k):
                    return False

            #check column
            for m in range(9):
                if board[m][j] == str(k):
                    return False

            cell_row = (i // 3) * 3
            cell_col = (j // 3) * 3

            for p in range(3):
                for q in range(3):
                    tmp_i = p + cell_row
                    tmp_j = q + cell_col

         
                    if board[tmp_i][tmp_j] == str(k):
                        return False

            
            return True

        
        #main sudoku solver function
        def ss(board,i,j):

            if i == 9:
                return True
            if j == 9:
                return ss(board,i+1,0)
         
            if board[i][j] == '.':
                for k in range(1,10):
                    if can_place(board,i,j,k):
                        board[i][j] = str(k)
                        tmp = ss(board,i,j+1)
                        if tmp:
                            return True

                board[i][j] = "."

                return False
            else:
                return ss(board,i,j+1)

        ss(board,0,0)
        
