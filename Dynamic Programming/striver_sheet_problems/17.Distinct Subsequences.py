#Leetcode - https://leetcode.com/problems/distinct-subsequences/description/

#Kind of include - exclude. start at the end of the both strings. if current char of both strings math we have 2 options - consider the matched char as a part of subsequence and find the remaining subsequence in remaining s string or dont consider this matched char as a part of matched subsequence and only move string s pointer 1 back and if char dont match then we have to reduce both the pointers.


#Memoization - top down
class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        mem = {}
        def func(i,j):

            if (i,j) not in mem:
                if j == 0:
                    mem[(i,j)] = 1
                elif i == 0:
                    mem[(i,j)] = 0

                elif s[i-1] == t[j-1]:
                    mem[(i,j)] = func(i-1,j-1) + func(i-1,j)
                else:
                    mem[(i,j)] = func(i-1,j)

            return mem[(i,j)]

        return func(len(s),len(t))


#Tabulation - bottom up
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        m = len(s)
        n = len(t)
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(m+1):
            dp[0][i] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[n][m]
        
