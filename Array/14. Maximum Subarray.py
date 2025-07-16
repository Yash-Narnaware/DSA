#Leetcode - https://leetcode.com/problems/maximum-subarray/description/

#Use kadane's algorithm.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum1 = 0
        res = float('-inf')

        for i in range(len(nums)):
            sum1 += nums[i]
            res = max(res, sum1)

            if sum1 < 0:
                sum1 = 0

        return res

        
