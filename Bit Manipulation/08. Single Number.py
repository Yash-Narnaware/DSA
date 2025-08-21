#Leetcode - https://leetcode.com/problems/single-number/description/

#Since XOR is 0 when bits are same => if numbers are same then xor must be 0. therefore xor entire array that way only unique element will be left since every other element will form 0 combibing to their pair.
#and 0 ^ num = num

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0
        for i in nums:
            res ^= i
        return res
        
