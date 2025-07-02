#Leetcode - https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

#Iterate through all substrings keep frequency count of current substring calculate min and max frequency and add its difference to result.


class Solution:
    def beautySum(self, s: str) -> int:
        
        res = 0
        count = {}
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                if s[j] in count:
                    count[s[j]] += 1
                else:
                    count[s[j]] = 1

                res += max(count.values()) - min(count.values())
            count = {}
        return res


#Another approach is to iterate over all substrings in a different way
class Solution:
    def beautySum(self, s: str) -> int:
        
        res = 0
        count = Counter(s)
        n = len(s)

        for i in range(n):
            temp = count.copy()
            for j in range(n-1, i-1, -1):
                res += max(count.values()) - min(count.values())
                count[s[j]] -= 1
                if count[s[j]] == 0:
                    del count[s[j]]
            temp[s[i]] -= 1
            if temp[s[i]] == 0:
                del temp[s[i]]
            count = temp.copy()

        return res
