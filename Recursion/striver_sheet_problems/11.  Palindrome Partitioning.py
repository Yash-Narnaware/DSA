#Leetcode - https://leetcode.com/problems/palindrome-partitioning/description/

#Iterate from 1st to last index+1 and only partition the string if left of idx is palindrome and then call function on remaining string.

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s):
            return s == s[::-1]
        
        n = len(s)
        def func(idx, current, res):

            if idx == n:
                res.append(current[:])
                return 

            for i in range(idx+1, n+1):
                if is_palindrome(s[idx:i]):
                    current.append(s[idx:i])
                    func(i, current, res)
                    current.pop()

        res = []
        func(0, [], res)

        return res
