#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

#Same as stocks part 2 just when you sell the stock call recursive function on index cur+2 instead of cur+1


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        mem = {}
        def func(cur, can_buy):

            if cur >= n:
                return 0

            if (cur, can_buy) in mem:
                return mem[(cur, can_buy)]

            if can_buy:

                buy = func(cur+1, False) - prices[cur]
                dont_buy = func(cur+1, True)

                res = max(buy, dont_buy)

            else:

                sell = func(cur+2, True) + prices[cur]
                dont_sell = func(cur+1, False)

                res = max(sell, dont_sell)


            mem[(cur, can_buy)] = res
            return mem[(cur, can_buy)]

        return func(0,True)



        
