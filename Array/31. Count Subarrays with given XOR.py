#GFG - https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1

#again very similar to counting subarrays with sum k just a XOR version of it.

class Solution:
    def subarrayXor(self, arr, k):

        map1 = {0: 1}
        xor = 0
        res = 0
        
        for i, j in enumerate(arr):
            xor ^= j
            if xor^k in map1:
                res += map1[xor^k]
            
            if xor in map1:
                map1[xor] += 1
            else:
                map1[xor] = 1
        
        return res
            
