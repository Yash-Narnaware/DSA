#leetcode - https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:

        mem = {}
        def func(n):
            if n not in mem:
                if n < 0:
                    mem[n] = 0
                else:
                    mem[n] = max(nums[n] + func(n-2), func(n-1))
            return mem[n]

        return func(len(nums)-1)
        
