#Leetcode - https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        palin = set([(i,i) for i in range(n)])

        res = (0,0)

        for lenght in range(2, n+1):
            for end in range(lenght-1, n):
                s1 = end - lenght + 1
                
                if s[s1] == s[end]:
                    if lenght == 2:
                        palin.add((s1,end))
                        res = (s1,end)

                    if (s1+1, end - 1) in palin:
                        res = (s1,end)
                        palin.add((s1,end))

        return s[res[0]: res[1]+1] 



        
        
