#GFG - https://www.geeksforgeeks.org/problems/rod-cutting0840/1


#Given a rod of lenght n and price for each piece size from 1 to n return the maximum price we can get after we cut it.

#Recursively call func for rod len n and try to cut at every size and add price of that cut size and call func on remaining portion. take max value of price for each cut.


#Recursive approach
class Solution:
    def cutRod(self, price):
     
        def func(n):
            
            if n == 0:
                return 0
            
            res = 0
            for i in range(1,n+1):
                res = max(res,price[i-1] + func(n-i))
                
            return res
            
        return func(len(price))



#Memoization - top down
class Solution:
    def cutRod(self, price):
     
        mem = {}
        def func(n):
            
            if n not in mem:
                if n == 0:
                    mem[n] = 0
                
                res = 0
                for i in range(1,n+1):
                    res = max(res,price[i-1] + func(n-i))
                mem[n] = res
                
            return mem[n]
            
        return func(len(price))


#Tabulation - bottom up
class Solution:
    def cutRod(self, price):
     
        n = len(price)
        dp = [0]*(n+1)
        
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i] = max(dp[i],price[j-1] + dp[i-j])
                
        return dp[n]

