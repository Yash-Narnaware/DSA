#GFG - https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

#given n matrix we can partition it in n-1 ways. - 1st matrix X result of remaining matrix multiplication, multi. of first 2 matrices X result of remaining matrix multiplication
#So at each step recursively call func to calculation operations required by rach partition and take minumum of it. 
#At each step number of operations is operations to multiply left partition + operations to multiply right partition + operations to multiply resultants of these partitions.



#Recursive approach
class Solution:
    def matrixMultiplication(self, arr):

        def func(i,j):
            
            #only have 1 matrix left
            if i+1 == j:
                return 0
            
            res = float('inf')
            #Calculating for each partition
            for k in range(i+1,j):
                
                res = min(res, func(i,k) + func(k,j) + arr[i]*arr[k]*arr[j])
                
            return res
            
        return func(0,len(arr)-1)
                
        


#Memoization - Top down
class Solution:
    def matrixMultiplication(self, arr):

        mem = {}
        def func(i,j):
            
            #only have 1 matrix left
            if i+1 == j:
                return 0
            
            if (i,j) not in mem:
                res = float('inf')
                #Calculating for each partition
                for k in range(i+1,j):
                    
                    res = min(res, func(i,k) + func(k,j) + arr[i]*arr[k]*arr[j])
                    
                mem[(i,j)] = res
            
            return mem[(i,j)]


#Tabulation - Bottom up
class Solution:
    def matrixMultiplication(self, arr):

        n = len(arr)
        dp = [[0]*n for _ in range(n)]

        for gap in range(2,n):
            for i in range(n-gap):
                j = i + gap
                
                dp[i][j] = float('inf')
                for k in range(i+1,j):
                    
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + arr[i]*arr[j]*arr[k])
                    
        return dp[0][n-1]
            
            
        return func(0,len(arr)-1)
                
        
        
