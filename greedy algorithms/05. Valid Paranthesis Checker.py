#Leetcode - https://leetcode.com/problems/valid-parenthesis-string/description/

#use 2 stacks 1 for ( pos and one for * pos and when ) occurs first pop from ( stack if not available then pop from * stack else return False. then if ( remains make sure for each rmaining ( we have * right to it.

class Solution:
    def checkValidString(self, s: str) -> bool:

        stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            else:
                star_stack.append(i)

        if not stack:
            return True

        for i in range(len(stack)-1, -1, -1):
            if not star_stack:
                return False
            if star_stack[-1] > stack[i]:
                star_stack.pop()
            else:
                return False
        return True
        
