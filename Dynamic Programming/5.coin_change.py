#Leetcode - coin change 2 - https://leetcode.com/problems/coin-change-ii/

#core logic is include - exclude coins, similar to knapsack problem


#Recursive function
def cnt_ways(sum1,coins,n):

    if sum1 == 0:
        return 1
    if n == 0 or sum1 < 0:
        return 0

    return cnt_ways(sum1 - coins[n-1],coins,n) + cnt_ways(sum1,coins,n-1)


#Tabulation approach(bottom-up)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1

        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]

       
        return dp[len(coins)][amount]


#Memoization approach(Top-down)
memo = {}
def cnt_ways(sum1,coins,n):

    if sum1 == 0:
        return 1
    if n == 0 or sum1 < 0:
        return 0

    #currently we are calculating for (sum1,n)
    if (sum1,n) in memo:
        return memo[(sum1,n)]
            
    include = cnt_ways(sum1 - coins[n-1],coins,n)
    exclude = cnt_ways(sum1,coins,n-1)

    memo[(sum1,n)] = include + exclude

    return memo[(sum1,n)]

return cnt_ways(amount,coins,len(coins))
