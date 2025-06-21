#Leetcode - https://leetcode.com/problems/wildcard-matching/description/


#write a recursive function given 2 pointers at the end of both strings. if current char matches or is equal to '?' then we can call func(i-1,j-1) because it matched. if char is '*' then we have to try to match it will every other char of 2nd string and see if we can make that string for this also we have to make recursive call(also for loop can be used) '*' can be empty so consider star empty and write func params accordingly + consider star as 1 char at a time(move other string index by 1 and dont move star index). if char is not ? or * and it doesnt match then just return False
#Carefully make base cases - if both i == 0and j == 0 then return True. but in one string we have just stars and in other nothing then they match cause star can be empty. so write testcase according to this.


#Recursive Approach
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def func(i,j):

            if i == 0 and j == 0:
                return True
            if i > 0 and j == 0:
                return False
            if j > 0 and i == 0:
                for i in range(j):
                    if p[i] != '*':
                        return False
                return True

            if p[j-1] == s[i-1] or p[j-1] == '?':
                return func(i-1,j-1)          
            elif p[j-1] == '*':
                return func(i,j-1) or func(i-1,j)
            else:
                return False

        return func(len(s),len(p))


#Memoization - top down
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        def func(i,j):

            if (i,j) not in mem:
                if i == 0 and j == 0:
                    mem[(i,j)] = True
                elif i > 0 and j == 0:
                    mem[(i,j)] = False
                elif j > 0 and i == 0:
                    not_star = False
                    for i in range(j):
                        if p[i] != '*':
                            not_star = True
                    
                    if not_star:
                        mem[(i,j)] = False
                    else:
                        mem[(i,j)] = True

                elif p[j-1] == s[i-1] or p[j-1] == '?':
                    mem[(i,j)] = func(i-1,j-1)          
                elif p[j-1] == '*':
                    mem[(i,j)] = func(i,j-1) or func(i-1,j)
                else:
                    mem[(i,j)] = False

            return mem[(i,j)]

        return func(len(s),len(p))


#Tabulation - bottom up
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        dp = [[False]*(n+1) for _ in range(m+1)]

        dp[0][0] = True

        for i in range(1,m+1):
            dp[i][0] = False

        for i in range(1,n+1):
            not_star = False
            for j in range(i):
                    if p[j] != '*':
                        not_star = True
            if not_star:
                dp[0][i] = False
            else:
                dp[0][i] = True



        for i in range(1,m+1):
            for j in range(1,n+1):

                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]          
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False

        return dp[m][n]

        
