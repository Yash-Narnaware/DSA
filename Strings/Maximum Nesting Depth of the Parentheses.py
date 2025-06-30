#Leetcode - https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:

        res = 0
        dp = 0

        for i in s:
            if i == '(':
                dp += 1
                res = max(dp, res)
            elif i == ')':
                dp -= 1
        return res
        
