#Leetcode - https://leetcode.com/problems/asteroid-collision/description/

#Use stack and keep storing same direction asteroids and then when collision can happen(stack value > 0 and current value < 0) then check abs values to pop the elements.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in asteroids:
            while stack and ((stack[-1] > 0 and i < 0)) and abs(stack[-1]) < abs(i):
                stack.pop()

            if stack:
                if abs(stack[-1]) > abs(i) and (stack[-1] > 0 and i < 0):
                    continue
                if abs(stack[-1]) == abs(i) and (stack[-1] > 0 and i < 0):
                    stack.pop()
                else:
                    stack.append(i)

            else:
                stack.append(i)

        return stack
        
