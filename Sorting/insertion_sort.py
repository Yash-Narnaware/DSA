# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
 
        n = len(arr)
        for i in range(1, n):
            j = i - 1
            temp = arr[i]

            while j >= 0 and arr[j] > temp:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = temp

        return arr
