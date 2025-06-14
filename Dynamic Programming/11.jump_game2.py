# Leetcode - https://leetcode.com/problems/jump-game-ii/description/

#return minimum number of jumps to reach last index from index 0. element at each index denotes the jump size.

#Start from TARGET and traverse all prev indices and recursively call func on only those indices who can reach current index. Say for index n we have 3 previous indices from which we can reach n then take their minimum+1 as minimum number of steps to reach index n.


#recursive solution
class Solution:
    def jump(self, nums: List[int]) -> int:


        #n is the index we want to reach
        def func(n):
            if n == 0:
                return 0

            res = float('inf')
            for i in range(n):
                if i + nums[i] >= n:
                    r1 = func(i)
                    res = min(res,r1+1)

            return res

        return func(len(nums)-1)


#memoixation(top-down)
class Solution:
    def jump(self, nums: List[int]) -> int:


        mem = {}

        #n is the index we want to reach
        def func(n):

            if n == 0:
                return 0
            if n not in mem:
                res = float('inf')
                for i in range(n):
                    if i + nums[i] >= n:
                        r1 = func(i)
                        res = min(res,r1+1)

                mem[n] = res
            return mem[n]

        return func(len(nums)-1)


#tabulation - (bottom up)
class Solution:
    def jump(self, nums: List[int]) -> int:


        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0

        for i in range(1,n):
            for j in range(i):
                if j + nums[j] >= i:
                    if dp[j] != float('inf'):
                        dp[i] = min(dp[i],dp[j] + 1)

        return dp[-1]

