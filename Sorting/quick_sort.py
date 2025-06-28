class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
            loc = self.partition(arr, low, high)
            self.quickSort(arr, low, loc-1)
            self.quickSort(arr, loc+1, high)
    
    def partition(self,arr,low,high):
 
        pivot = arr[high]
        start = low
        end = high - 1
        
        while True:
            
            while start <= end and arr[start] <= pivot:
                start += 1
                
            while start <= end and arr[end] > pivot:
                end -= 1
                
            if end <= start:
                break
                
            arr[start], arr[end] = arr[end], arr[start]
            
        arr[high], arr[start] = arr[start], arr[high]
        
        return start
    
