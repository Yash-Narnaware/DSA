#GFG - https://www.geeksforgeeks.org/problems/geeks-training/1


class Solution:
    def maximumPoints(self, arr):
  
        n = len(arr)
        mem = {}
        def func(n,activity):
            
            if (n,activity) not in mem:
                if n == 0:
                    mem[(n,activity)] = 0
                
                else:    
                    res = 0
                    for act in range(3):
                        if activity != act:
                            res = max(res,arr[n-1][act] + func(n-1, act))
                    
                    mem[(n,activity)] = res
                        
            return mem[(n,activity)]
                    
                
        return max(func(n,0),func(n,1),func(n,2))
                
