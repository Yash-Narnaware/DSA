#GFG - https://www.geeksforgeeks.org/problems/sort-a-stack/1

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):

        def temp(s, x):
            if not s or s[-1] < x:
                s.append(x)
            else:
                tmp = s.pop()
                temp(s, x)
                s.append(tmp)
    
        def func(s):
            
            if s:
                x = s.pop()
                func(s)
                temp(s, x)
          
        func(s)

            
            
