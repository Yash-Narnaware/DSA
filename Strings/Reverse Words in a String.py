#Leetcode - https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0
        res = []

        while i < n:
            if s[i] != " ":
                tmp = ""
                while i < n and s[i] != " ":
                    tmp += s[i]
                    i += 1
                res.append(tmp)
            
            i += 1 

        return " ".join(res[::-1])
        
