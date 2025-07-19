#Leetcode - https://leetcode.com/problems/set-matrix-zeroes/description/

#Approach 1: using row and column set to determine which rows and columns need to be zeroed then in next traversal zero those row and column elements.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row = set()
        zero_col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0

        

#Approach 2: in place modification - store wheather to zero that column or row in first row and column. have to use extra variable to store the status of row 0 or column 0 since they overlap. After recording this set the zeros in matrix except forst row and column and then at last set the values of 1st row and column(remember the order setting zero order matters for 1st row and column depending on the extra variable you have chosen)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0

                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != 0:    
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        print(i, j)
                        matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        if col0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        
        
