#GFG - https://www.geeksforgeeks.org/problems/top-k-frequent-elements-in-array/1

import heapq
class Solution:
	def topKFrequent(self, arr, k):

		freq = {}
		
		for i in arr:
		    if i in freq:
		        freq[i] += 1
		    else:
		        freq[i] = 1
		        
        tmp = []
        
        for ke, v in freq.items():
            tmp.append((-v, -ke))
            
        heapq.heapify(tmp)
        
        res = []
        
        for i in range(k):
            res.append(-heapq.heappop(tmp)[1])
            
        return res


#Approach 2 - sorting
        
		
		
