#TUF - https://takeuforward.org/plus/dsa/problems/next-smaller-element

class Solution:
    def nextSmallerElements(self, arr):
        # Your code goes here
      n = len(arr)
	    res = [-1]*n
	    stack = []
		
		for i in range(n - 1, -1, -1):
		    while stack and arr[i] <= stack[-1]:
		        stack.pop()
	        
	        if stack:
	            res[i] = stack[-1]
	        else:
	            #no need for this else because of array initialization just added for better understanding
	            res[i] = -1
	        stack.append(arr[i])
	        
	    return res
