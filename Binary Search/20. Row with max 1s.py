#GFG - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

class Solution:
    def rowWithMax1s(self, arr):

        row = len(arr)
        col = len(arr[0])
        
        res = -1
        max_one = 0
        
        for i in range(row):
            tmp = arr[i]
            l = 0
            r = col - 1
            
            while l <= r:
                mid = (l + r) // 2
                
                if tmp[mid] == 1:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            ones = 0
            if l != col:
                ones = col - l
                
            if ones > max_one:
                max_one = ones
                res = i
                
        return res
                
