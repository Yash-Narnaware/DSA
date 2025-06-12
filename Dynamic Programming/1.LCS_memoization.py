#LCS memoization(Top down) solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        mem = {}
        
        def lcs(m,n):

            if (m,n) not in mem:
                if m == len(text1) or n == len(text2):
                    mem[(m,n)] = 0
                    return mem[(m,n)]

                if text1[m] == text2[n]:
                    res = 1 + lcs(m+1,n+1)
                else:
                    res = max(lcs(m+1,n), lcs(m,n+1))
                mem[(m,n)] = res
            return mem[(m,n)]

        return lcs(0,0)
        
