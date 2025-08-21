#GFG - https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1


#Setting the rightmost bit
class Solution:
	def setBit(self, n):
		# code here
		i = 0
		while n >> i & 1 == 1:
		    i += 1
		    
	    return n + 2**i

#Unsetting the rightmost bit - bitwise & with n - 1 since it will set the rightmost set bit to zero

return n & (n - 1)
		    
		
