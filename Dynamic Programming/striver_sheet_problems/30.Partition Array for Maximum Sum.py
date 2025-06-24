#Leetcode - https://leetcode.com/problems/partition-array-for-maximum-sum/description/


#Similar as palindrome partitioning. iterate from index 0 to forward at each index try all possible partitions sizes till size k calculate value for formed partition and recursively call function on remaining array and choose maximum between all the partition values.


#Memoization - top down
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        mem = {}
        def func(i):

            if i == n:
                return 0

            if i in mem:
                return mem[i]

            max1 = float('-inf')
            res = float('-inf')
            for j in range(i,min(i+k,n)):
                max1 = max(max1,arr[j])

                res = max(res, max1*(j-i+1) + func(j+1))

            mem[i] = res
            return mem[i]

        return func(0)



#Tabulation - bottom up
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            max1 = float('-inf')
            res = float('-inf')
            for j in range(i,min(i+k,n)):
                max1 = max(max1,arr[j])

                res = max(res, max1*(j-i+1) + dp[j+1])

            dp[i] = res

        return dp[0]

        
