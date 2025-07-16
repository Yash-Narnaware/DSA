#Leetcode - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        buy = 0

        for sell in range(1, len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                res = max(res, prices[sell] - prices[buy])

        return res
        
