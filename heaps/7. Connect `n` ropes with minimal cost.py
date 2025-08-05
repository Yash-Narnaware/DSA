#GFG - https://www.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

#General way of thinking is select 2 minimum elements and connect them this minimizes the difference between max and min elements and reduces the overall cost to combine them.

import heapq
class Solution:
   def minCost(self, arr):

    cost = 0
    heapq.heapify(arr)
    
    while arr:
        a = heapq.heappop(arr)
        if not arr:
            return cost
        b = heapq.heappop(arr)
        
        cost += (a+b)
        
        heapq.heappush(arr, a+b)
    
