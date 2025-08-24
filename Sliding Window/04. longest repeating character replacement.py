#Leetcode - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

#keep the frequency dict and for each window calculat the max freq in current window and according to that canculate the replacements required for making that window elelements equal to max freq elem. if it is > k then shrink the window from left(start).


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        cur_freq = {}

        start, end = 0, 0
        res = 0
        # max_freq = 0

        while end < len(s):

            if s[end] in cur_freq:
                cur_freq[s[end]] += 1
            else:
                cur_freq[s[end]] = 1

            max_freq = 0

            # max_freq = max(max_freq, cur_freq[s[end]])

            for k1, v in cur_freq.items():
                max_freq = max(max_freq, v)

            replacement_needed = end - start + 1 - max_freq

            # print(replacement_needed, k)

            if replacement_needed <= k:
                res = max(res, end - start + 1)
            else:
                cur_freq[s[start]] -= 1
                start += 1
            
            end += 1

        return res
        
