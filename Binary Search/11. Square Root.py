#GFG - https://www.geeksforgeeks.org/problems/square-root/1

class Solution:
    def floorSqrt(self, n): 
        l = 1
        r = n
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid*mid == n:
                return mid
            
            if mid*mid > n:
                r = mid - 1
            else:
                l = mid + 1
                
        return r
            
