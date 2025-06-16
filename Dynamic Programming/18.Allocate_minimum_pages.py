#GFG - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1


#solution - consider partitioning at every place possible and recursively call func for partitioned array for 1 less student(k), we want max sum of this partitions over minimum.


#Recursive approach
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        
        def func(n,k):
            
            if k == 1:
                return sum(arr[:n])
            if n == 1:
                return arr[0]
                
            if k > n:
                return -1
            
            res = float('inf')
            for i in range(1,n):
                
                res = min(res,max(func(i,k-1),sum(arr[i:n]))) 
                
            return res
            
        return func(len(arr),k)

    
      
#Memoization - top down
#Recursive approach
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        
        mem = {}
        def func(n,k):
            
            if (n,k) not in mem:
                if k > n:
                   mem[(n,k)] = -1 
                elif n == 1:
                    mem[(n,k)] = arr[0]
                    
                elif k == 1:
                    mem[(n,k)] = sum(arr[:n])
                    
                
                else:
                    res = float('inf')
                    for i in range(1,n):
                        
                        res = min(res,max(func(i,k-1),sum(arr[i:n]))) 
                    mem[(n,k)] = res
                    
            return mem[(n,k)]
            
        return func(len(arr),k)


#Tabulation - bottom up
class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        
        n = len(arr)
        
        if k > n:
            return -1 
            
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + arr[i]
            
        def range_sum(i, j):  # sum of arr[i:j]
            return prefix_sum[j] - prefix_sum[i]
        
        dp = [[0]*(n+1) for _ in range(k+1)]
        
        
        for j in range(n+1):
            dp[1][j] = prefix_sum[j]
            
        for i in range(k+1):
            dp[i][1] = arr[0]
            
        for i in range(2,k+1):
            for j in range(2,n+1):
                
                dp[i][j] = float('inf')
                for p in range(1,j):
                    dp[i][j] = min(dp[i][j],max(dp[i-1][p], range_sum(p,j)))
                    
        return dp[k][n]

#even better solution is possible using binary search.
