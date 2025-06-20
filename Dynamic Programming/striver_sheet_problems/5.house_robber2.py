#Leetcode - https://leetcode.com/problems/house-robber-ii/submissions/1670357274/

#Similar to house robber 1 just houses are in circle so first and last house are adjecent

#Just consider 2 arrays 1 w/o first element and 1 w/o last element and calculate the answer and return their max value. Since robber cant rob 1st and last house together so we are removing possibility of that happening.

class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        def func(n,arr):

            if n not in mem:
                if n < 0:
                    mem[n] = 0
                else:
                    mem[n] = max(arr[n] + func(n-2,arr), func(n-1,arr))

            return mem[n]
        
        mem = {}
        res1 = func(n-2,nums[1:])

        mem = {}
        res2 = func(n-2,nums[:-1])

        return max(res1, res2)
        
