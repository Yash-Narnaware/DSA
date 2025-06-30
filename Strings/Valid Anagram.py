#Leetcode - https://leetcode.com/problems/valid-anagram/description/

#If non ascii chars are present then we can use frequency dictionary for both strings and then compare both the dicts. for anagram they should be equal.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        map_s = [0]*26
        map_t = [0]*26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            map_s[ord(s[i]) - ord('a')] += 1
            map_t[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if map_s[i] != map_t[i]:
                return False

        return True

        
