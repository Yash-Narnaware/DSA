#GFG - https://www.geeksforgeeks.org/problems/target-sum-1626326450/1




#recursive approach
class Solution:
    def findTargetSumWays(self, n, arr, target):
        
        def func(sum1,n):
            
            if n == 0:
                if (sum1) == target:
                    return 1
                else:
                    return 0
         
            return func(sum1 + arr[n-1],n-1) + func(sum1 - arr[n-1],n-1)

        return func(0,len(arr))

#Memoization - Top down
class Solution:
    def findTargetSumWays(self, n, arr, target):
        
        mem = {}
        def func(sum1,n):
            
            if (sum1,n) not in mem:
                if n == 0:
                    if (sum1) == target:
                        mem[(sum1,n)] = 1
                    else:
                        mem[(sum1,n)] = 0
                else:        
                    mem[(sum1,n)] = func(sum1 + arr[n-1],n-1) + func(sum1 - arr[n-1],n-1)
            
            return mem[(sum1,n)]
            
        return func(0,len(arr))
