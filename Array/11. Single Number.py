#Leetcode - https://leetcode.com/problems/single-number/description/

#Use XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0
        for i in nums:
            res ^= i
        return res
        
