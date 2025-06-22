#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

#At each index consider all the possibilities like buy,sell, do nothing and move to nex index. if we already have bought the stock then selling it at current index or moving to next index etc.


#Recursive Approach
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def func(cur,bought):

            if cur == n:
                return 0
            if bought != -1:
                return max(prices[cur] - prices[bought], func(cur+1,bought))
            else:
                return max(func(cur+1,cur), func(cur+1,bought))

        return func(0,-1)


#Memoization - top down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        mem = {}
        def func(cur,bought):
            if (cur, bought) not in mem:
                if cur == n:
                    mem[(cur, bought)] = 0

                elif bought != -1:
                    mem[(cur, bought)] = max(prices[cur] - prices[bought], func(cur+1,bought))

                else:
                    mem[(cur, bought)] = max(func(cur+1,cur), func(cur+1,bought))

            return mem[(cur, bought)]

        return func(0,-1)



      
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


  
