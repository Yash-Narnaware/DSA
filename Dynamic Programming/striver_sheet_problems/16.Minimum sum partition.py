#GFG - https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1

#Find if sum of subsets from 0 to sum(arr) is possible or not - use tabulation store true/False values for sum and n


class Solution:
	def minDifference(self, arr):


        n = len(arr)
        m = sum(arr)
        
        dp = [[False]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
            
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
                
        
        res = float('inf')
        for i,j in enumerate(dp[n]):
            if j == True: 
                res = min(res, abs(m - 2*i))
        
        return res




