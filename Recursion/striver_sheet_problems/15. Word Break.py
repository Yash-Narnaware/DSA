#Leetcode - https://leetcode.com/problems/word-break/description/

#DP problem. - struggled to get what base case is and what to return. we want at least one way so or function calls we res which is initialized to False. if we reach end of the string then return True
#From starting index check if substring is in wordDict if yes then call function on remaing string. instead of 1 characted at a time at any index we can iterate through wordDict and directly check if word is equal to first n(size of word in wordDict) chars of string if yes then call func on remaining string

#Memoization.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        n = len(s)
        mem = {}
        def func(idx):
            if idx == n:
                return True

            if idx in mem:
                return mem[idx]

            res = False
            for i in range(idx+1, n+1):
                if s[idx:i] in wordDict:
                    res = res or func(i)

            mem[idx] = res
            return mem[idx]

        return func(0)
