#Leetcode - https://leetcode.com/problems/count-number-of-nice-subarrays/

#Same as previous one just count number of odds in this problem instread of keeping track of current sum.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:


        start, end, tmp = 0, 0, 0
        res = 0
        odd = 0
        while end < len(nums):

            if nums[end] % 2 == 1:
                odd += 1


            while start < end and odd > k:
                if nums[start] % 2 == 1:
                    odd -= 1
                start += 1
                tmp = start

            if odd == k:
                while tmp < end and nums[tmp] % 2 == 0:
                    tmp += 1

                res += (tmp - start + 1)

            end += 1

        return res
        
