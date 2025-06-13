#GFG - https://www.geeksforgeeks.org/problems/cutted-segments1642/1


#Recursive solution

# My initial approach - 

class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        
        def func(n,x,y,z,segs):
            
            if n == 0:
                return segs
            if n < 0:
                return 0
            
            return max(
                func(n-x,x,y,z,segs+1),
                func(n-y,x,y,z,segs+1),
                func(n-z,x,y,z,segs+1))
            
        
        return func(n,x,y,z,0)


#Improved recursive approach - removing segs as a parameter since in every call we dont need it. just incrementing it if segmentation is possible

class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        
        def func(n,x,y,z):
            
            if n == 0:
                return 0
            if n < 0:
                return -1
            
            res = max(
                func(n-x,x,y,z),
                func(n-y,x,y,z),
                func(n-z,x,y,z))
            
            if res == -1:
                return -1
            else:
                return res + 1
            
        
        res = func(n,x,y,z)
        return res if res != -1 else 0



#Memoization(Top-down)

class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        
        memo = {}
        def func(n,x,y,z):
            
            if n not in memo:
                if n == 0:
                    return 0
                if n < 0:
                    return -1
                    
                res = max(
                    func(n-x,x,y,z),
                    func(n-y,x,y,z),
                    func(n-z,x,y,z))
                
                if res == -1:
                    memo[n] = -1
                else:
                    memo[n] = res + 1
            
            return memo[n]
            
        
        res = func(n,x,y,z)
        return res if res != -1 else 0



#Tabulation(bottom up)
# dp[i] is maximum partitions possible till rod lenght i
class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        
        dp = [0]*(n+1)
        #this dp[0] = 1 because if we reach zero we found 1 way/segmentation(later we will reduced it from final result)
        #if we dont put this then dp[i-x] != 0 these type of conditions wont make it possible to reach 0 and if we remove these conditions then say even if dp[5] = 0 and we are calculating dp[7] and one of the cuts leads to dp[5] then even if dp[5] = 0 dp[7] will be 1 from this cut which is incorrect as there are no valid cuts from 5 and dp[7] is being calculated 1 indicating 1 segmentation is possible.
        # Another simpler way can be initialize dp[0] = 0 and all other indices to be -1 and remove all dp[] != 0 conditions
        dp[0] = 1
        
        for i in range(1,n+1):
            if i - x >= 0 and dp[i-x] != 0:
                dp[i] = max(dp[i],dp[i-x] + 1)
            if i - y >= 0 and dp[i-y] != 0:
                dp[i] = max(dp[i],dp[i-y] + 1)
            if i - z >= 0 and dp[i-z] != 0:
                dp[i] = max(dp[i],dp[i-z] + 1)
                
        
        return dp[-1] - 1 if dp[-1] != 0 else 0




#simplified version of above code - 
class Solution:
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        
        dp = [-1]*(n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            if i - x >= 0:
                dp[i] = max(dp[i],dp[i-x])
            if i - y >= 0:
                dp[i] = max(dp[i],dp[i-y])
            if i - z >= 0:
                dp[i] = max(dp[i],dp[i-z])
                
            if dp[i] != -1:
                dp[i] += 1
                
        return dp[-1] if dp[-1] != -1 else 0
