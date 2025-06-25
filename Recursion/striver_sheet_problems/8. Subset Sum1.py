#GFG - https://www.geeksforgeeks.org/problems/subset-sums2234/1

class Solution:
	def subsetSums(self, arr):
	
		n = len(arr)
		def func(n1, current_sum, res):
		    
		    if n1 == n:
		        res.append(current_sum)
		        return
		    
		    #include
		    func(n1 + 1, current_sum + arr[n1], res)
		    
		    #exclude
		    func(n1 + 1, current_sum, res)
		    
		 
		res = []
		func(0, 0, res)
		
		return res
