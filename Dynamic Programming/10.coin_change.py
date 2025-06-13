# Leetcode - https://leetcode.com/problems/coin-change/

# Given coins return the minimum number of coins to make up the given amount
#Consider using each coin at any amount and recursively call func again on amount = amount - coin value


#recursive approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def func(amount,coins):

            if amount < 0:
                return float('inf')

            if amount == 0:
                return 0

            res = float('inf')
            for i in coins:
                res1 = func(amount - i,coins)
                res = min(res,res1+1)

            return res

        res = func(amount,coins)
        return res if res != float('inf') else -1



#meoization - top-down approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        mem = {}
        def func(amount,coins):

            if amount not in mem:
                if amount < 0:
                    return float('inf')

                if amount == 0:
                    return 0

                res = float('inf')
                for i in coins:
                    res1 = func(amount - i,coins)
                    res = min(res,res1+1)

                mem[amount] = res

            return mem[amount]

        res = func(amount,coins)
        return res if res != float('inf') else -1



#tabulation - bottom up
# dp[i] is the minimum number of coins required to make amount i.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float('inf')]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            tmp = float('inf')
            for j in coins:
                if i - j >= 0:
                    tmp = min(tmp,dp[i - j])

            dp[i] = tmp + 1

        
        return dp[-1] if dp[-1] != float('inf') else -1

        

        


