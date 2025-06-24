#Leetcode - https://leetcode.com/problems/burst-balloons/description/

#Think reverse what would be the case when only 1 balloon left then what would be scenario when last 2 balloon are left.


class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums.insert(0,1)
        nums.append(1)

        mem = {}
        def func(i,j):

            if i > j:
                return 0

            if (i,j) in mem:
                return mem[(i,j)]

            res = float('-inf')
            for k in range(i,j+1):

                res = max(res, func(i,k-1) + func(k+1,j) + nums[i-1]*nums[k]*nums[j+1])

            mem[(i,j)] = res
            return mem[(i,j)]

        return func(1,len(nums)-2)


#Tabulation
n = len(nums)
nums.insert(0,1)
nums.append(1)

dp = [[0]*(n+2) for _ in range(n+2)] 

for i in range(n,0,-1):
    for j in range(1,n+1):
        if i > j:
            continue

        res = float('-inf')
        for k in range(i,j+1):
            res = max(res, dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1])

        dp[i][j] = res

return dp[1][n]
