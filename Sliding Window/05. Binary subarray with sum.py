#Leetcode - https://leetcode.com/problems/binary-subarrays-with-sum/description/

#add end element to current sum then move start ptr till cur sum > goal and then calculate the subarrays for cur_sum == goal.

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        start, end, tmp = 0, 0, 0
        res = 0
        sum1 = 0
        while end < len(nums):
            sum1 += nums[end]

            while start < end and sum1 > goal:
                    sum1 -= nums[start]
                    start += 1
                    tmp = start

            if sum1 == goal:
                while tmp < end and nums[tmp] == 0:
                    tmp += 1

                res += (tmp - start + 1)

            end += 1

        return res
        
