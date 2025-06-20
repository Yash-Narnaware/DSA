#Leetcode - https://leetcode.com/problems/minimum-path-sum/description/


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        mem = {}
        def func(m,n):

            if (m,n) not in mem:
                if m == 0 or n == 0:
                    mem[(m,n)] = float('inf')
                elif m == 1 and n == 1:
                    mem[(m,n)] = grid[0][0]
                else:
                    mem[(m,n)] = min(func(m-1,n) + grid[m-1][n-1], func(m,n-1) + grid[m-1][n-1]) 
            
            return mem[(m,n)]

        return func(len(grid), len(grid[0]))



#Tabulation - bottom up
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = float('inf')

        for i in range(n+1):
            dp[0][i] = float('inf')

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[0][0]
                else:
                    dp[i][j] = min(dp[i-1][j] + grid[i-1][j-1], dp[i][j-1] + grid[i-1][j-1]) 


        return dp[m][n]
