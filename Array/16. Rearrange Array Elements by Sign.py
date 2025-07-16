#Leetcode - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

#create a res array of size n and keep 2 pointers even = 0 and odd = 1 initially, then traverse through nums and if positive number appeas then insert it at index even in res and increase even by 2 and same for odd.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        res = [0]*len(nums)
        even = 0
        odd = 1

        for i in nums:
            if i > 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
        return res
        
