#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

#iterate through all the indices for each index we can buy or sell stock. pass can_buy parameter so that we can know if we can sell/buy stock or not  

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        n = len(prices)
        mem = {}
        def func(cur, can_buy):
            
            if cur == n:
                return 0

            if (cur, can_buy) in mem:
                return mem[(cur, can_buy)]

            profit = -1
            
            if can_buy:
                buy = func(cur+1, False) - prices[cur]  
                not_buy = func(cur+1,True)

                profit = max(buy, not_buy)

            else:

                sell = prices[cur] + func(cur+1,True)
                not_sell = func(cur+1,False)

                profit = max(sell,not_sell)

            mem[(cur, can_buy)] = profit
            return mem[(cur, can_buy)]

        return func(0,True)

        

