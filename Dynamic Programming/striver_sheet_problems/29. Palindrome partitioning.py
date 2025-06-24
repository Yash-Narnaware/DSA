#Leetcode - https://leetcode.com/problems/palindrome-partitioning-ii/description/

#Here I have done it using iD dp approach. at each index if left substring of the index is palindrome then return 1 + partition_count_on_right_substring
#We are substracting 1 from answer because we are adding extra 1 partition at the end which is not needed.


#memoization - top down
class Solution:
    def minCut(self, s: str) -> int:

        def is_palindrome(s):
            return s == s[::-1]
        
        n = len(s)
        mem = {}
        def func(i):

            if i == n:
                return 0

            if i in mem:
                return mem[i]
            res = float('inf')
            for k in range(i+1,n+1):
                if is_palindrome(s[i:k]):
                    res = min(res, func(k) + 1)

            mem[i] = res
            return res

        return func(0) - 1


#Bottom up - Tabulation
class Solution:
    def minCut(self, s: str) -> int:

        def is_palindrome(s):
            return s == s[::-1]

        n = len(s)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            res = float('inf')
            for k in range(i+1,n+1):
                if is_palindrome(s[i:k]):
                    res = min(res, dp[k] + 1)

            dp[i] = res

        return dp[0] - 1

        
