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
#TBD
