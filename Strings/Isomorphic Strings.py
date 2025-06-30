#Leetcode - https://leetcode.com/problems/isomorphic-strings/description/

#Map each char of s to t. create a dictionary for mapping. if char in s is already in dict then its val should be equal to current t[i]. and if s[i] not in dict then we should not have mapped anything to char t[i] also(keep a set for seen t[i]) since we cant map different chars to same char in t.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        map = {}
        n = len(s)
        seen = set()

        for i in range(n):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in seen:
                    return False
                map[s[i]] = t[i]
                seen.add(t[i])

        return True
        
