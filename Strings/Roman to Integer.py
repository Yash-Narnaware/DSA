#Leetcode - https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:

        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = mapping[s[-1]]
        n = len(s)

        for i in range(n-2,-1,-1):
            if mapping[s[i+1]] > mapping[s[i]]:
                res -= mapping[s[i]]
            else:
                res += mapping[s[i]]

        return res



        
