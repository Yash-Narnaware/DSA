#GFG - https://www.geeksforgeeks.org/problems/set-bits0143/1

#We can do it by bruteforce or use Brian and kanningham's algorithm.(bitwose & of n with n - 1 removes the rightmost set bit from n. so do it till n > 0)
#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		res = 0
		
		while n > 0:
		    n = n & (n - 1)
		    res += 1
		    
	    return res


#Another similar problem
#GFG - https://www.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
#Will do it later
#Here we can calculate the number 
