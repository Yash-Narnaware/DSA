#GFG - https://www.geeksforgeeks.org/problems/unique-bsts-1587115621/1

#Easy way is to return the catalan number
#To use DP consider each node as a root and return (unique BST on left nodes * unique BST on right nodes) keep adding these results for each n

#Recursive approach
class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):
        
        if n == 0 or n == 1:
            return 1
            
        res = 0
        for i in range(n):
            res += self.numTrees(n-i-1) * self.numTrees(i)
        return res



#Memoization - Top down
class Solution:
    #Function to return the total number of possible unique BST.
    mem = {}
    def numTrees(self,n):
        
        if n not in self.mem:
            if n == 0 or n == 1:
                self.mem[n] = 1
            else:    
                res = 0
                for i in range(n):
                    res += self.numTrees(n-i-1) * self.numTrees(i)
                self.mem[n] = res
        
        return self.mem[n]



#Tabulation - Bottom up
class Solution:
    #Function to return the total number of possible unique BST.
    def numTrees(self,n):
 
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] = 0
            for j in range(i):
                dp[i] += dp[i-j-1] * dp[j]
                
        return dp[n]
