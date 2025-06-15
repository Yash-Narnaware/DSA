#GFG - https://www.geeksforgeeks.org/problems/palindromic-patitioning4845/1

#Variant of matrix chain multiplication problem. Just base case is return 0 if string is palindrome.


#Recursive approach
class Solution:
    def palPartition(self, s):

        def func(i,j):
            #base case - if string is palindrome we need 0 partitions.
            if s[i:j+1] == s[i:j+1][::-1]:
                return 0
            
            res = float('inf')
            for k in range(i+1,j):
                #no. of minimum partitions to partition left partition + no. of minimum partitions to partition right partition + 1 for partitioning the whole string into left and right partition
                res = min(res,func(i,k)+func(k+1,j)+1)
                
            return res
            
        return func(0,len(s)-1)


#Memoization - Top down
class Solution:
    def palPartition(self, s):

        
        def is_palindrome(l,r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        mem = {}
        def func(i,j):
            
            if (i,j) not in mem:
                #base case - if string is palindrome we need 0 partitions.
                if is_palindrome(i,j):
                    mem[(i,j)] = 0
                else:
                    res = float('inf')
                    for k in range(i+1,j):
                        res = min(res,func(i,k)+func(k+1,j)+1)
                        
                    mem[(i,j)] = res
                
            return mem[(i,j)]
            
        return func(0,len(s)-1)


#Tabulation - bottom up
class Solution:
    def palPartition(self, s):

        
        def is_palindrome(l,r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        for gap in range(1,n):
            for i in range(n-gap):
                j = i + gap
                
                if is_palindrome(i,j):
                    dp[i][j] = 0
                else:
                    dp[i][j] = float('inf')
                    for k in range(i,j):
                        
                        dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + 1)
                    
        return dp[0][n-1]
