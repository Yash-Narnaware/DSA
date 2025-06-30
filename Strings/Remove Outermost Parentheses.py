#Leetcode - https://leetcode.com/problems/remove-outermost-parentheses/description/

#Primitive string found when #open brackets = #close brackets

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        #Primitive string found when #open brackets = #close brackets
        idx = 0
        open = close = 0

        res = ''
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            else:
                close += 1

            if open == close:
                res += s[idx+1:i]
                idx = i + 1

        return res
        
