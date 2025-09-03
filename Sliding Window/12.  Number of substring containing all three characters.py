#Leetcode - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

#Use hashmap to keep track whether all required alphabets are present in current window or not when len(freq_map) == 3 then all 3 chars are present in that case count the total number of substrings possible for current window.

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        freq = {}
        res = 0
        start, end = 0, 0

        while end < len(s):
            if s[end] in freq:
                freq[s[end]] += 1
            else:
                freq[s[end]] = 1

            while len(freq) == 3:
                res += (len(s) - end)
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1
                
            end += 1

        return res
