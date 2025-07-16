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


#Printing maximum subarray - just keep track of start and end inex of max sum subarray using 2 variables and only update them when you found new max sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum1 = 0
        res = float('-inf')
        mx_start, mx_end = 0,0
        temp_start = 0

        for i in range(len(nums)):
            sum1 += nums[i]
            if sum1 > res:
                mx_end = i
                mx_start = temp_start
                res = sum1

            if sum1 < 0:
                temp_start = i+1
                sum1 = 0
        
        print(nums[mx_start:mx_end+1])

        return res

        


        
