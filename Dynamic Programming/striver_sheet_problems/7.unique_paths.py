#Leetcode - https://leetcode.com/problems/unique-paths/submissions/1670404914/
#DP on grid

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mem = {}
        def func(m,n):
            if (m,n) not in mem:
                if m <= 0 or n <= 0:
                    mem[(m,n)] = 0
                elif m == 1 and n == 1:
                    mem[(m,n)] = 1
                else:
                    mem[(m,n)] = func(m-1,n) + func(m,n-1)
            return mem[(m,n)]

        return func(m,n)


#Tabulation
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,n+1):
            dp[1][i] = 1
        for i in range(1,m+1):
            dp[i][1] = 1

        for i in range(2,m+1):
            for j in range(2,n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m][n]
