#GFG - https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1

class Solution:
    def generateBinaryStrings(self, n):

        def func(n1, can_one, current, res):
            
            if n1 == n:
                res.append(current)
                return 
            
            func(n1+1, True, current + '0', res)
            
            if can_one:
                func(n1+1, False, current + '1', res)
                
        res = []
        func(0,True,'',res)
        
        return res
                
            
                
            
