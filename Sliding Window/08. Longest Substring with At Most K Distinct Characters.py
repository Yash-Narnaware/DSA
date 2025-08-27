#TUF - https://takeuforward.org/plus/dsa/problems/longest-substring-with-at-most-k-distinct-characters

class Solution:
    def kDistinctChar(self, s, k):

        max_len = 0
        start, end = 0, 0

        cur_freq = {}

        while end < len(s):

            if s[end] in cur_freq:
                cur_freq[s[end]] += 1
            else:
                if len(cur_freq) < k:
                    cur_freq[s[end]] = 1
                else:
                    max_len = max(max_len, end - start)

                    while len(cur_freq) == k:
                        cur_freq[s[start]] -= 1
                        if cur_freq[s[start]] == 0:
                            del cur_freq[s[start]]
                        start += 1

                    cur_freq[s[end]] = 1


            end += 1

        max_len = max(max_len, end - start)

        return max_len
