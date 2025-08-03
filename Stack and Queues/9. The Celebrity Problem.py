#GFG - https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

#Simple matrix traversal problem

class Solution:
    def celebrity(self, mat):

        n = len(mat)
        for i in range(n):
            tmp = True
            for j in range(n):
                if i != j and (mat[i][j] != 0 or mat[j][i] == 0):
                    tmp = False
                    break
            if tmp:
                return i
                
        return -1
