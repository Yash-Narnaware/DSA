#Leetcode - https://www.geeksforgeeks.org/problems/replace-elements-by-its-rank-in-the-array/1

#Store the index of each element in dict. element --> indices(elements can be repeated) then create min hep from all the unique elements and callculate the ranks using min heap and count variable.

#User function Template for python3
import heapq
class Solution:
    def replaceWithRank(self, N, arr):

        #element -> idx
        mapping = {}
        
        min_hp = []
        
        for i, j in enumerate(arr):
            if j in mapping:
                mapping[j].append(i)
            else:
                min_hp.append(j)
                mapping[j] = [i]
                
        heapq.heapify(min_hp)
        
        cnt = 0
        while min_hp:
            element = heapq.heappop(min_hp)
            cnt += 1
            for i in mapping[element]:
                arr[i] = cnt
                
        return arr
                
        
