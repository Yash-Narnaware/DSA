#Leetcode - https://leetcode.com/problems/triangle/submissions/1670587504/


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        mem = {}
        def func(i,j):

            if (i,j) not in mem:
                if j < 0 or j >= len(triangle[i]):
                    mem[(i,j)] = 0 
                elif i == m - 1:
                    mem[(i,j)] = triangle[i][j]
                else:
                    mem[(i,j)] = min(func(i+1, j), func(i+1, j+1)) + triangle[i][j] 

            return mem[(i,j)]

        return func(0,0)



#Tabulation - bottom up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m = len(triangle)
        dp = [[0]*i for i in range(1,m+1)]

        for i in range(m):
            dp[m-1][i] = triangle[m-1][i]

        for i in range(m-2,-1,-1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

        return dp[0][0]
        
