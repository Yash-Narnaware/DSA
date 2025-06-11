# Variants of Longest Common Subsequence (LCS)

## 1. Minimum Insertions and Deletions to Convert S1 to S2

### Problem Link
[LeetCode: Minimum Insertions and Deletions](https://leetcode.com/problems/delete-operation-for-two-strings/)

### Description
Given two strings `s1` and `s2`, find the minimum number of insertions and deletions required to convert `s1` into `s2`. This can be solved using the LCS of the two strings. The number of deletions is the length of `s1` minus the length of LCS, and the number of insertions is the length of `s2` minus the length of LCS.

### Solution
1. Compute the LCS of `s1` and `s2` using dynamic programming.
2. Calculate deletions: `len(s1) - LCS_length`.
3. Calculate insertions: `len(s2) - LCS_length`.

### Code
```python
#This leetcode problem is minute variate of what we discussed above - in this we have to make both strings same and we only have deletion operation and we have to return the minimum number of deletions required to mke both strings equal. 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return m + n - 2*dp[m][n]
```

## 2. Shortest Common Supersequence

### Problem Link
[LeetCode: Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)

### Description
Given two strings `s1` and `s2`, find the shortest string that has both `s1` and `s2` as subsequences. The length of the shortest common supersequence (SCS) is `len(s1) + len(s2) - LCS_length`. The actual supersequence can be constructed by backtracking the LCS DP table.

### Solution
1. Compute the LCS DP table for `s1` and `s2`.
2. Backtrack through the DP table to construct the SCS by including non-matching characters from both strings and common characters once.

### Code
```python
def shortestCommonSupersequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Construct SCS
    i, j = m, n
    result = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
            result.append(s1[i-1])
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or dp[i][j] == dp[i-1][j]):
            result.append(s1[i-1])
            i -= 1
        else:
            result.append(s2[j-1])
            j -= 1
            
    return ''.join(result[::-1])
```

## 3. Longest Palindromic Subsequence

### Problem Link
[LeetCode: Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

### Description
Given a string `s`, find the length of the longest palindromic subsequence in `s`. This can be solved by finding the LCS of `s` and its reverse, as the longest palindromic subsequence is the longest common subsequence between the string and its reverse.

### Solution
1. Create the reverse of string `s`.
2. Compute the LCS of `s` and its reverse using dynamic programming.
3. The length of the LCS is the length of the longest palindromic subsequence.

### Code
```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        n = m
        text1 = s
        text2 = s[::-1]
        dp = [[0]*(n+1) for _ in range(m+1)]


        for i in range(1,m+1):
            for j in range(1,n+1):

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        
        return dp[m][n]
        
```

## 4. Longest Repeating Subsequence

### Problem Link
[GeeksforGeeks: Longest Repeating Subsequence](https://www.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1)

### Description
Given a string `s`, find the length of the longest subsequence that appears at least twice in `s` with no overlapping characters. This is solved by finding the LCS of `s` with itself, ensuring that the same index is not used for matching characters.

### Solution
1. Compute the LCS of `s` with itself.
2. Modify the LCS logic to ensure that characters at the same index (`i == j`) are not considered for matching.

### Code
```python
class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
		
		m = len(s)
        n = m
        text1 = s
        text2 = s
        dp = [[0]*(n+1) for _ in range(m+1)]


        for i in range(1,m+1):
            for j in range(1,n+1):

                if text1[i-1] == text2[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        
        return dp[m][n]
```

## 5. Space Optimized DP Solution of LCS

### Problem Link
[GeeksforGeeks: Space Optimized LCS](https://www.geeksforgeeks.org/space-optimized-solution-lcs/)

### Description
Given two strings `s1` and `s2`, find the length of their longest common subsequence using a space-optimized dynamic programming approach. Instead of using an `m x n` DP table, use two arrays of size `n` to reduce space complexity from O(m*n) to O(n).

### Solution
1. Use two arrays of size `n+1` to store the current and previous rows of the DP table.
2. Alternate between these arrays while computing the LCS.
3. The final value in the current array gives the LCS length.

### Code
```python
def lcsSpaceOptimized(s1, s2):
    m, n = len(s1), len(s2)
    if m < n:
        s1, s2 = s2, s1
        m, n = n, m
    
    curr = [0] * (n + 1)
    prev = [0] * (n + 1)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev = curr[:]
    
    return curr[n]
```
