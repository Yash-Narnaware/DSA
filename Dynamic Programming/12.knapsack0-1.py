#GFG - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1


#solution - include exclude problem. consider each subset and take max value subset as an answer

 
#recusive approach - when include some element add its value in include variable and reduce is weight from current capacity. And handle case where weight of current item > current capacity(exclude that item and return function without that item)
#in base case n == -1 because i am passing n - index of element. therefore item at index should must also be processed.
class Solution:
    def knapsack(self, W, val, wt):
        
        def knap(W,n):
            
            if W == 0 or n == -1:
                return 0
            
            if wt[n] > W:
                return knap(W,n-1)
            else:
                include = val[n] + knap(W-wt[n],n-1) 
                exclude = knap(W,n-1)
            
            return max(include, exclude)
            
        return knap(W,len(val)-1)



#memoization - (Top-down)
class Solution:
    def knapsack(self, W, val, wt):
        
        mem = {}
        def knap(W,n):
            
            if W == 0 or n == -1:
                return 0
                
            if (W,n) not in mem:
                if wt[n] > W:
                    mem[(W,n)] = knap(W,n-1)
                else:
                    include = val[n] + knap(W-wt[n],n-1) 
                    exclude = knap(W,n-1)
                
                    mem[(W,n)] = max(include, exclude)
            return mem[(W,n)]
            
        return knap(W,len(val)-1)


#tabulation - (bottom up)
class Solution:
    def knapsack(self, W, val, wt):
        #W*n
        n = len(val)
        dp = [[0]*(n+1) for _ in range(W+1)]
        
        
        for i in range(1,W+1):
            for j in range(1,n+1):
                if wt[j-1] > i:
                    dp[i][j] = dp[i][j-1]
                else:
                    #same logic as recursion - max of include,exclude
                    dp[i][j] = max(val[j-1] + dp[i-wt[j-1]][j-1], dp[i][j-1])
                    
        return dp[W][n]
            


