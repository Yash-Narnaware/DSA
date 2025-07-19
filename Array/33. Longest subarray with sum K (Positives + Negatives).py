#GFG - https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

#Again very similar to longest subarray with sum 0 problem.

class Solution:
    def longestSubarray(self, arr, k):  
        
        map1 = {0: -1}
        res = 0
        sum1 = 0
        
        for i, j in enumerate(arr):
            sum1 += j
            
            if sum1 - k in map1:
                res = max(res, i - map1[sum1 - k])
            
            if sum1 not in map1:
                map1[sum1] = i
        
        return res
            
    
