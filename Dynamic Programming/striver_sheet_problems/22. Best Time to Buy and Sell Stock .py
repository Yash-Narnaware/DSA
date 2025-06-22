#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

#same as prevois part just instead of 2 transactions we can complete at most k transactions - just change the base condition.

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        mem = {}
        def func(cur, can_buy, transaction):

            if transaction == k or cur == n:
                return 0

            if (cur, can_buy, transaction) in mem:
                return mem[(cur, can_buy, transaction)]

            if can_buy:
                buy = func(cur+1, False, transaction) - prices[cur]
                dont_buy = func(cur+1, True, transaction)

                res = max(buy, dont_buy)

            else:
                sell = func(cur+1, True, transaction+1) + prices[cur]
                dont_sell = func(cur+1, False, transaction)

                res = max(sell, dont_sell)

            mem[(cur, can_buy, transaction)] = res
            return mem[(cur, can_buy, transaction)]

        return func(0,True,0)
        
