#GFG - https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
		l = 1
		r = m
		
		while l <= r:
		    
		    mid = (l + r) // 2
		    
		    if mid**n == m:
		        return mid
		        
		    if mid**n > m:
		        r = mid - 1
		    else:
		        l = mid + 1
		        
	    return -1
