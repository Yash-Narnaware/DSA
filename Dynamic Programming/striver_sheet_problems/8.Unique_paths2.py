#Leetcode - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        mem = {}
        def func(m,n):
            if (m,n) not in mem:
                if m <= 0 or n <= 0 or obstacleGrid[m-1][n-1] == 1:
                    mem[(m,n)] = 0
                elif m == 1 and n == 1:
                    mem[(m,n)] = 1
                else:
                    mem[(m,n)] = func(m-1,n) + func(m,n-1)
            return mem[(m,n)]

        return func(m,n)



#Tabulation
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*(n) for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = 0
                    left = 0
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left

        return dp[m-1][n-1]

        
