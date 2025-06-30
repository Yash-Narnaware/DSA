#Leetcode - https://leetcode.com/problems/sort-characters-by-frequency/description/

#Learned about lambda function and how to sorta dict

class Solution:
    def frequencySort(self, s: str) -> str:

        mp = Counter(s)
        a = sorted(mp.items(), key=lambda item: item[1], reverse=True)
        res = []

        for char, freq in a:
            res.append(char*freq)
        
        return ''.join(res)
        
