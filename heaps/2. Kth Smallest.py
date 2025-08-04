#GFG - https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1

import heapq
class Solution:

    def kthSmallest(self, arr,k):
        
        heapq.heapify(arr)
        
        for i in range(k - 1):
            heapq.heappop(arr)
        return arr[0]
        
