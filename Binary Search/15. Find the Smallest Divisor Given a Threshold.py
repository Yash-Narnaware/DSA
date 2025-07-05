#Leetcode - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def calc_sum(divisor):
            res = 0
            for i in nums:
                res += ceil(i / divisor)

            return res

        l = 1
        r = max(nums)

        while l <= r:  
            mid = (l + r) // 2
            if calc_sum(mid) <= threshold:
                r = mid - 1
            else:
                l = mid + 1

        return l
        
