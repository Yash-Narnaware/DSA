#Leetcode 72 - https://leetcode.com/problems/edit-distance/description/
#Description - given 2 strings s1 and s2 have to convert s1 to s2 using 3 operations - insert,delete,replace. return minimum number of operations.


#Similar to LCS just when current index chars are equal we dont have to perform any operation and when then are not equal then return minimum number of operation required amongst performing each operation i.e. insertion,deletion and replaement(similar to returning max() in LCS) 


#Recursive solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def ed(w1,w2,m,n):
            if m == 0:
                return n
            if n == 0:
                return m

            if w1[m-1] == w2[n-1]:
                return ed(w1,w2,m-1,n-1)
            
            return 1 + min(ed(w1,w2,m,n-1), ed(w1,w2,m-1,n), ed(w1,w2,m-1,n-1))

        return ed(word1,word2,len(word1),len(word2))




#Memoization - Top down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        mem = {}
        def ed(w1,w2,m,n):
            if m == 0:
                return n
            if n == 0:
                return m

            if (m,n) not in mem:
                
                if w1[m-1] == w2[n-1]:
                    mem[(m,n)] = ed(w1,w2,m-1,n-1)
                else:
                    insert = ed(w1,w2,m,n-1)
                    delete1 = ed(w1,w2,m-1,n)
                    replace = ed(w1,w2,m-1,n-1)

                    mem[(m,n)] = 1 + min(insert,delete1,replace)
                    
            return mem[(m,n)]

        return ed(word1,word2,len(word1),len(word2))




#Tabulation (Bottom up)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                if j == 0:
                    dp[i][j] = i
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    insert = dp[i][j-1]
                    delete = dp[i-1][j]
                    replace = dp[i-1][j-1]

                    dp[i][j] = 1 + min(insert,delete,replace)

        return dp[m][n]


        

