#GFG - https://www.geeksforgeeks.org/problems/maximum-sum-combination/1

#sort the arrays in reverse order and in heap with sum also add the indices of elements from which you computed the sum and for each pair we put in heap we have to consider indices i+1, j and i, j+1 for maximum sum at that point.

import heapq
class Solution:
    def topKSumPairs(self, a, b, k):

        a.sort(reverse=True)
        b.sort(reverse=True)
        
        i, j = 0, 0
        
        tmp = [(-(a[0] + b[0]), (0,0))]
        heapq.heapify(tmp)
        
        st = set()
        
        res = []
        
        for i in range(k):
            val, (x, y) = heapq.heappop(tmp)
            res.append(-val)
            
            
            if (x + 1, y) not in st and x + 1 < len(a):
                st.add((x + 1, y))
                heapq.heappush(tmp, (-(a[x + 1] + b[y]), (x + 1, y)))
            if (x, y + 1) not in st and y + 1 < len(b):
                st.add((x, y + 1))
                heapq.heappush(tmp, (-(a[x] + b[y + 1]), (x, y + 1)))
            
        
        return res    
        
