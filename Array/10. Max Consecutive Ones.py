#Leetcode - https://leetcode.com/problems/max-consecutive-ones/description/

#Use 2 pointer approach

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        idx = 0
        for cur in range(n):
            if nums[cur] == 0:
                res = max(res, cur - idx)
                idx = cur + 1
        if nums[-1] == 1:
            res = max(res, cur - idx + 1)
        
        return res
        
