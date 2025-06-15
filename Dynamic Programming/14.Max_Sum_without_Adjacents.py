# GFG - https://www.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1

#Given an array find the maximum subsequence sum possible s.t. no two element in that subsequence should be adjecent

#Similar to include-exclude problem. For considering each such subsequence whenever we include current element in a sum call func on element which is before the prevois element(1st non-adjecent element)


#Recursive approach
class Solution:
	
	def findMaxSum(self,arr):
		def func(arr,n):
		    if n < 0:
		        return 0        
		    return max(arr[n] + func(arr,n-2), func(arr,n-1))
		
		return func(arr,len(arr)-1)

#Memoization(Top-down)
class Solution:
	
	def findMaxSum(self,arr):

		mem = {}
		def func(arr,n):
		    
		    if n < 0:
		        return 0
		        
		    if n not in mem:
		    
		        res = max(arr[n] + func(arr,n-2), func(arr,n-1))
		        mem[n] = res
		    return mem[n]
		    
		
		return func(arr,len(arr)-1)

#Tabulation(Bottom up)
#dp[i] is max sum till ith index
class Solution:
	
	def findMaxSum(self,arr):

		dp = [0]*(len(arr)+1)
		dp[1] = arr[0]
		
		for i in range(2,len(arr)+1):
		    
		    dp[i] = max(dp[i-1],arr[i-1]+dp[i-2])
		    
		
		return max(dp)
