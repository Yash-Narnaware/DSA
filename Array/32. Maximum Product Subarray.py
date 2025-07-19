#Leetcode - https://leetcode.com/problems/maximum-product-subarray/description/

#very obsevation based. consider each scenario - all postive, all negative, even number of negatives, odd number of negatives. if odd negatives we have to drop any one negative. if any case solution must be from prefix or suffix product. chose max between them. if 0 occures just reset the prefix or suffix product to 1 respectively,

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float('-inf')
        n = len(nums)
        pre = 1
        post = 1

        for i, j in enumerate(nums):
            pre *= j
            post *= nums[n - 1 - i]
            res = max(res, max(pre, post))

            if pre == 0:
                pre = 1
            if post == 0:
                post = 1

        return res
        
