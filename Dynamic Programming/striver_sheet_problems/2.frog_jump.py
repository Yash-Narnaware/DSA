#GFG - https://www.geeksforgeeks.org/problems/geek-jump/1



#User function Template for python3
class Solution:
    def minCost(self, height):

        mem = {}
        def min_jumps(n):

            if n not in mem:
                if n == 0:
                    mem[n] = 0
                elif n == 1:
                    mem[n] = abs(height[0] - height[1])
                else:    
                    one_jmp = min_jumps(n-1) + abs(height[n] - height[n-1])
                    two_jmp = min_jumps(n-2) + abs(height[n] - height[n-2])

                    mem[n] = min(one_jmp, two_jmp)
            return mem[n]
            
        return min_jumps(len(height)-1)


#Tabulation
#User function Template for python3
class Solution:
    def minCost(self, height):

        dp = [0]*len(height)
        if len(height) <= 1:
            return 0
        
        dp[1] = abs(height[0] - height[1])
        
        for i in range(2,len(height)):
            dp[i] = min(dp[i-1]+abs(height[i]-height[i-1]),dp[i-2]+abs(height[i]-height[i-2])) 
            
        return dp[-1]
