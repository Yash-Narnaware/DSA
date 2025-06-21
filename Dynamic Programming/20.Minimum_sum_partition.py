#GFG - https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1

#Description - given a list return the minimum difference possible of sum of elements of 2 subsets of list(partition)

#Solution - calculate the subarray sum - include - exclude and when we reach base case i.e. n == 0 return the absolute difference between 2 partitions 1st one is sum of subarray itsef and 2nd one is total array sum - subarray sum that we calculated


#Recursive approach
class Solution:
	def minDifference(self, arr):

		def func(sum1,n):
		    
		    if n == 0:
		      #abs(sum1 - (array sim - sum1))  
          return abs(2*sum1 - sum2)
		        
		    return min(func(sum1+arr[n-1], n-1), func(sum1, n-1))
		  
		sum2 = sum(arr)
		
		return func(0,len(arr))


#Memoization - Top-down
class Solution:
	def minDifference(self, arr):

		mem = {}
		def func(sum1,n):
		    
		    if (sum1,n) not in mem:
    		    if n == 0:
    		        mem[(sum1,n)] = abs(2*sum1 - sum2)
    		        
    		    else:
    		        mem[(sum1,n)] = min(func(sum1+arr[n-1], n-1), func(sum1, n-1))
    		        
    	    return mem[(sum1,n)]
		       
		sum2 = sum(arr)
		
		return func(0,len(arr))


#Tabulation - bottom up

#Find if sum of subsets from 0 to sum(arr) is possible or not - use tabulation store true/False values for sum and n
#then iterate through last row of dp table and if that sum is possible using that sum compute other partition sum and find the minimum abs difference


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
