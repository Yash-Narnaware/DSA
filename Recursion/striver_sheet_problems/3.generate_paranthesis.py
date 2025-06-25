#Leetcode - https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def func(n1, current, open, close, res):

            if n1 == 2*n:
                res.append(current)
                return
    
            if open < n:
                func(n1 + 1, current + '(', open + 1, close, res)

            if open > close:
                func(n1 + 1, current + ')', open, close + 1, res)

        res = []
        func(0, '', 0, 0, res)

        return res

