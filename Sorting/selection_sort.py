class Solution: 
    def selectionSort(self, arr): 
        n = len(arr)
        for i in range(n-1):
            temp_min = i
            for j in range(i+1, n):
                if arr[j] < arr[temp_min]:
                    temp_min = j

            arr[i], arr[temp_min] = arr[temp_min], arr[i]

        return arr
