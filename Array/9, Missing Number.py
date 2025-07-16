#Leetcode - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        sm1 = (n**2 + n) // 2
        sm2 = sum(nums)

        return sm1 - sm2


#Another approach is to use XOR operation slightly better than above approach because sum of array can be very large but XOR value will not exceed the n.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        xor1, xor2 = 0, 0

        for i in range(n):
            xor2 ^= nums[i]
            xor1 ^= (i+1)
        
        return xor1 ^ xor2
