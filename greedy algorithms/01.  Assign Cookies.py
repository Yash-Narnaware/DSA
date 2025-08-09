#Leetcode - https://leetcode.com/problems/assign-cookies/

#sort the array and then check the given condition

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort(reverse=True)
        s.sort(reverse=True)

        i, j = 0, 0
        res = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
                j += 1
            else:
                i += 1
        
        return res
        
