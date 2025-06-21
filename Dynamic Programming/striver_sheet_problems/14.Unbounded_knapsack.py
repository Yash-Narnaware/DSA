#GFG - https://www.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1


class Solution:
    def knapSack(self, val, wt,capacity):
 
        # mem = {}
        # def func(W,n):

        #     if (W,n) not in mem:
        #         if W == 0 or n == 0:
        #             mem[(W,n)] = 0
    
        #         else:
        #             include = 0
        #             if W >= wt[n-1]:
        #                 include = func(W - wt[n-1],n) + val[n-1]
        #             exclude = func(W ,n-1)
        #             mem[(W,n)] = max(include,exclude)
                    
        #     return mem[(W,n)]

        # return func(capacity,len(val))
        
        
        n = len(val)
        
        dp = [[0]*(capacity+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,capacity+1):
                include = 0
                if j >= wt[i-1]:
                    include = dp[i][j - wt[i-1]] + val[i-1]
                exclude = dp[i-1][j]
                dp[i][j] = max(include,exclude)
                
        return dp[n][capacity]
