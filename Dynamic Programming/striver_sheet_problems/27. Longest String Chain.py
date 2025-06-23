#Leetcode - https://leetcode.com/problems/longest-string-chain/description/

#Sort the words according to their lenght
#write similar code to LIS just need to check if jth element is predecessor of ith element.

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        

        def custom_sort(n):
            return len(n)

        def is_predecessor(w1,w2):

            i = len(w1) - 1
            j = len(w2) - 1

            mismatched = False
            res = True

            while i >= 0 and j >= 0:
                if w1[i] != w2[j]:
                    if mismatched:
                        res = False
                        break
                    else:
                        mismatched = True
                        i -= 1
                else:
                    i -= 1
                    j -= 1

            return res

        words.sort(key=custom_sort)

        n = len(words)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if len(words[j]) == len(words[i]) - 1 and is_predecessor(words[i], words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
