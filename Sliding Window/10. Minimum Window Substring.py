#Leetcode - https://leetcode.com/problems/minimum-window-substring/description/



#My initial brute force approach
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_freq = Counter(t)

        def check_same(tmp):
            for k, v in t_freq.items():
                if k not in tmp or tmp[k] < v:
                    return False
            return True
                
        start, end = 0, 0
        freq = {}
        res = float('inf')
        res_s, res_e = -1, -1
        while end < len(s):

            if s[end] in freq:
                freq[s[end]] += 1
            else:
                freq[s[end]] = 1

            while check_same(freq):
                if res > end - start + 1:
                    res = end - start + 1
                    res_s = start
                    res_e = end
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1

            end += 1

        return "" if res_s == -1 or res_e == -1 else s[res_s: res_e+1] 


#Approach 2: Instead of checking each time using check_same function we can keep track of currently how many elements satisfied the frequency condition and if it is equal to needed elements frequency then update the result.

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_freq = Counter(t)

        start, end = 0, 0
        freq = {}
        res = float('inf')
        res_s, res_e = -1, -1
        need = len(t_freq)
        have = 0
        while end < len(s):

            if s[end] in freq:
                freq[s[end]] += 1
            else:
                freq[s[end]] = 1

            if s[end] in t_freq and freq[s[end]] == t_freq[s[end]]:
                have += 1
            while have == need:
                if res > end - start + 1:
                    res = end - start + 1
                    res_s = start
                    res_e = end
                freq[s[start]] -= 1
                if s[start] in t_freq and freq[s[start]] < t_freq[s[start]]:
                    have -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1

            end += 1

        return "" if res_s == -1 or res_e == -1 else s[res_s: res_e+1] 

        
        
