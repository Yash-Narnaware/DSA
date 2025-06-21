#GFG - https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1


#No need to check till end of array. we just have to check if there exist a subset that sums up to target

class Solution:
    def isSubsetSum (self, arr, sum):
 
        mem = {}
        def func(sum1,n):
            
            if (sum1,n) not in mem:
 
                if sum1 == 0:
                    mem[(sum1,n)] = True
                elif sum1 < 0 or n == 0:
                        mem[(sum1,n)] = False
                else:        
                
                    mem[(sum1,n)] = func(sum1 - arr[n-1], n-1) or func(sum1,n-1)
                    
            return mem[(sum1,n)]
                
        return func(sum, len(arr))
        


#Tabulation - bottom up

        n = len(arr)
        
        dp = [[False]*(sum+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1,n+1):
            for j in range(1,sum+1):
                if j >= arr[i-1]:
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
                
        
        return dp[n][sum]
