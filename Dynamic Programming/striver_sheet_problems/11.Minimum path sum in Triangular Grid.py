#Leetcode - https://leetcode.com/problems/minimum-falling-path-sum/submissions/1670609936/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:


        n = len(matrix)
        mem = {}
        def func(i,j):

            if (i,j) not in mem:
                if j < 0 or j >= n:
                    mem[(i,j)] = float('inf')

                elif i == n-1:
                    mem[(i,j)] = matrix[i][j]
                else:
                    mem[(i,j)] = (min(func(i+1, j-1), func(i+1, j), func(i+1, j+1)) + matrix[i][j])
            return mem[(i,j)]

        res = float('inf')
        for i in range(n):
            res = min(res,func(0,i))

        return res



#Tabulation - Bottom up
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        dp = [[0]*n for _ in range(n)]

        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(n):

                left = dp[i+1][j-1] if j-1 >= 0 else float('inf')
                down = dp[i+1][j]
                right = dp[i+1][j+1] if j+1 < n else float('inf')

                dp[i][j] = min(left,down,right) + matrix[i][j]

        return min(dp[0])
        
