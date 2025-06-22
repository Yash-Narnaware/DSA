#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

#Same as part 2 just add 1 more parameter to track the number of transactions. When you sell stock then only increase the number of transactions.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        mem = {}
        def func(cur, can_buy, transaction):

            if transaction == 2 or cur == n:
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
        
