
#unoptimized version
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        n = len(arr)
        
        for i in range(n-1):
            for j in range(n-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

#Optimized version
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        n = len(arr)
        
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    swapped = True
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
            if not swapped:
                break
                    
        return arr
