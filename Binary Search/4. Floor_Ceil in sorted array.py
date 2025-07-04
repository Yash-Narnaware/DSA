#GFG - https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
#GFG - https://www.geeksforgeeks.org/problems/ceil-in-a-sorted-array/1


class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            
            mid = (l + r) // 2
            if arr[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
                
        return r


class Solution:
    def findCeil(self, arr, x):

        l = 0
        r = len(arr) - 1
        
        while l <= r:
            
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
                
        return l if l < len(arr) else -1
