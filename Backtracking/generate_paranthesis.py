#For a valid paranthesis only 1 codition is required i.e. no of ')' should always be less than or equal to '('
#and first keep adding '(' till its less than n.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        def gen(str1,i,open,close,res):

            if i == 2*n:
                res.append(str1)
                return

            if open < n:
                gen(str1 + '(',i+1,open+1,close,res)

            if close < open:
                gen(str1 + ')',i+1,open,close+1,res)

        res = []

        gen('',0,0,0,res)

        return res


            
