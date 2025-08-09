#GFG - https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1

#Heaps have property that parent should always be smaller or greater than their children(depending on min or max heap). so for each node check this property holds or not.


class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here   
        
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n:
                if arr[left] > arr[i]:
                    return 0
            if right < n:
                if arr[right] > arr[i]:
                    return 0
                    
        return 1
            
