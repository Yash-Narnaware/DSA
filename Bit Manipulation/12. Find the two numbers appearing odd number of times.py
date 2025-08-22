#Leetcode - https://leetcode.com/problems/single-number-iii/description/

#find xor of all array that way aat last wee will have xor of 2 distinct numbers. now rightmost set bit of xor value tells us the first bit of distinction between 2 distinct numbers. so we will divide numbers into 2 groups each group will have one of the distinct number since we will divide on basis of ith bit which we know is different in distinct numbers and then xor each number from that group and we will get 1st distinct number, xor nums from 2nd group and we will get 2nd distinct number.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        dist_elem_xor = 0

        for i in nums:
            dist_elem_xor ^= i
        
        i = 0
        while dist_elem_xor >> i & 1 == 0:
            i += 1
        
        num1 = 0
        num2 = 0

        for j in nums:
            if j >> i & 1 == 0:
                num1 ^= j
            else:
                num2 ^= j
        return [num1, num2]
        
