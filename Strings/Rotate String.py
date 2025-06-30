#Leetcode - https://leetcode.com/problems/rotate-string/description/

#Try to form every rotated string and compare it with goal if match return True

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        n1 = len(s)
        n2 = len(goal)

        if n1 != n2:
            return False

        for i in range(n1):
            if s[i:] + s[:i] == goal:
                return True

        return False

        
