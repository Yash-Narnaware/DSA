#GFG - https://www.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
    def getSecondLargest(self, arr):

        largest = arr[0]
        second_largest = -1
        
        for i in range(1, len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] > second_largest and arr[i] != largest:
                second_largest = arr[i]
        
        return second_largest
