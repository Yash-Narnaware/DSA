#GFG - https://www.geeksforgeeks.org/problems/nearly-sorted-1587115620/1

#For loop doesnt go outside its range - i mean the iterate will stop at last valid number not 1 more than that.

import heapq
class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        min_hp = arr[:k].copy()
        heapq.heapify(min_hp)
        
        for i in range(n - k):
            heapq.heappush(min_hp, arr[i+k])
            arr[i] = heapq.heappop(min_hp)
        while min_hp:
            i += 1
            arr[i] = heapq.heappop(min_hp)
            
            
