#GFG - https://www.geeksforgeeks.org/problems/implement-lower-bound/1

class Solution:
    def lowerBound(self, arr, target):
        n = len(arr)
        l = 0
        r = len(arr) - 1
        
        while l < r:
            
            mid = (l + r) // 2
            
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        return l if arr[l] >= target else n
