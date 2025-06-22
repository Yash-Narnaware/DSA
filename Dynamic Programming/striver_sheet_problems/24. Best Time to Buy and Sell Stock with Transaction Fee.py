#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

#Just substract fee whenever you buy/sell a stock. only one time substract this fee at buy or at sell.


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        mem = {}
        def func(cur, can_buy):

            if cur == n:
                return 0

            if (cur, can_buy) in mem:
                return mem[(cur, can_buy)]

            if can_buy:
                #changing fee when buying the stock
                buy = func(cur+1, False) - prices[cur] - fee
                dont_buy = func(cur+1, True)

                res = max(buy, dont_buy)

            else:

                sell = func(cur+1, True) + prices[cur]
                dont_sell = func(cur+1, False)

                res = max(sell, dont_sell)

            mem[(cur, can_buy)] = res
            return mem[(cur, can_buy)]

        return func(0, True)
        
