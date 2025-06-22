#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

#At each index consider all the possibilities like buy,sell, do nothing and move to nex index. if we already have bought the stock then selling it at current index or moving to next index etc.




#Memoization - top down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        mem = {}
        def func(cur, can_buy):

            if cur == n:
                return 0

            if (cur, can_buy) in mem:
                return mem[(cur, can_buy)]

            if can_buy:

                buy = func(cur+1, False) - prices[cur]
                dont_buy = func(cur+1, True)

                res = max(buy,dont_buy)

            else:

                sell = prices[cur]
                dont_sell = func(cur+1,False)

                res = max(sell, dont_sell)
            mem[(cur,can_buy)] = res
            return mem[(cur,can_buy)]           

        return func(0,True)




      
#This approaches gives TLE or memory limit reached

#Striver approach - from index 1 to n consider selling stock on each index and buying prices will be minimum price we saw till current index. have to maintain min_price and max_prof at each index.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        min_price = prices[0]

        max_prof = 0
        for i in range(1,n):
            max_prof = max(max_prof, prices[i] - min_price)
            min_price = min(min_price,prices[i])

        return max_prof


  
