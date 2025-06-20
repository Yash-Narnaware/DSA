class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        mem = {}
        def ways(n):
            if n not in mem:
                if n == 1:
                    mem[n] = 1
                elif n == 2:
                    mem[n] = 2
                else:
                    mem[n] = ways(n-1) + ways(n-2)
            return mem[n]

        return ways(n)



#Tabulation - bottom up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,2]
        for i in range(2,n):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n-1]
        
