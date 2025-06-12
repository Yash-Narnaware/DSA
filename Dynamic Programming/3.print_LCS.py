# LCS tabulation(bottom up) solution + printing LCS
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]


        for i in range(1,m+1):
            for j in range(1,n+1):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        lcs = ''
        #printing the LCS
        m1 = m
        n1 = n
        while m1 > 0 and n1 > 0:

            if text1[m1-1] == text2[n1-1]:
                lcs += text1[m1-1]
                m1 -= 1
                n1 -= 1
            else:
                if dp[m1-1][n1] >= dp[m1][n1-1]:
                    m1 = m1-1
                else:
                    n1 = n1 - 1

        print(lcs[::-1])

        
        return dp[m][n]



        
