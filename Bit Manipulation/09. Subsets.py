#Leetcode - https://leetcode.com/problems/subsets/description/

# Bizzare/mond blowing way to look at this problem - so if we want power set of some array of lenght n, total numre of subsets will be 2^n so if you think about it if we iterate from 0 to 2^n - 1 and represent each number in binary we can look at leftmost n bits and include the elements corresponding to set bits in current combination from nums
# in short write number of combination in binary and take set bit as include.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        for i in range(2**n):
            tmp = []
            for j in range(n):
                if i >> j & 1 == 1:
                    tmp.append(nums[j])
            res.append(tmp)

        return res 
        
