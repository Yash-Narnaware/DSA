#GFG - https://www.geeksforgeeks.org/problems/reverse-a-stack/1

from typing import List

class Solution:
    def reverse(self,St): 
 
        def insert_at_bottom(s,x):
            if not s:
                s.append(x)
            else:
                t = s.pop()
                insert_at_bottom(s,x)
                s.append(t)
        
        
        def rev(s):
            
            if s:
                x = s.pop()
                rev(s)
                insert_at_bottom(s,x)
                
        rev(St)
        return St
