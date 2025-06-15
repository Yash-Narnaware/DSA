#GFG - https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

#subset problem - include-exclude. given arr return no. of subsets whos element sum is equal to target.


#Recursive solution
class Solution:
	def perfectSum(self, arr, target):

        def func(sum1,n):
            #this base condition because we have to consider each element while forming subset
            # and element can be 0 so sum1 == 0 may not give all subsets. e.g.  arr = [28 4 3 27 0 24 26] sum = 24. so at current point even if sum1 == 0 we should check all the remaining elements.
            if n < 0:
                return 1 if sum1 == 0 else 0
                
            return(func(sum1 - arr[n],n-1) + func(sum1,n-1))
            
        
        return func(target,len(arr)-1)


#Memoization - Top down
class Solution:
	def perfectSum(self, arr, target):
        mem = {}
        def func(sum1,n):
            if n < 0:
                return 1 if sum1 == 0 else 0
                
            if (sum1,n) not in mem:
                mem[(sum1,n)] = (func(sum1 - arr[n],n-1) + func(sum1,n-1))
                
            return mem[(sum1,n)]
            
        return func(target,len(arr)-1)


#Tabulation - bottom up
class Solution:
	def perfectSum(self, arr, target):

        m = len(arr)
        n = target
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = 1
            
        for i in range(1,m+1):
            #J starts from 0 to handle 0 in array
            for j in range(n+1):
                if j < arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                
        return dp[m][n]
        
        
