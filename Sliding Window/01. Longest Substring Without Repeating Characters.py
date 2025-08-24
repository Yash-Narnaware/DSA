#Leetcode - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#Maintain a present set to store the elements present in current window and expand the window till same element present in window occur again then shrink from left till that element.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        present = set()
        start = 0
        res = 0
        for end in range(len(s)):
            if s[end] not in present:
                present.add(s[end])
            else:
                res = max(res, end - start)
                while s[start] != s[end]:
                    present.remove(s[start])
                    start += 1
                start += 1

        res = max(res, len(s) - start)

        return res
                
        
