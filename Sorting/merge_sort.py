class Solution:
 
    def mergeSort(self,arr, l, r):

        def merge(arr1, arr2):
            
            res = []
            
            n1 = len(arr1)
            n2 = len(arr2)
            
            ptr1 = 0
            ptr2 = 0
            
            while ptr1 < n1 and ptr2 < n2:
                if arr1[ptr1] >= arr2[ptr2]:
                    res.append(arr2[ptr2])
                    ptr2 += 1
                else:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                    
            while ptr1 < n1:
                res.append(arr1[ptr1])
                ptr1 += 1
                
            while ptr2 < n2:
                res.append(arr2[ptr2])
                ptr2 += 1
                
            return res
            
        def merge_sort(arr):
            
            if len(arr) <= 1:
                return arr
                
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
            
        return merge_sort(arr)




#In place(not entirely)
class Solution:
 
    def mergeSort(self,arr, l, r):

        def merge(arr, lb, mid, ub):
            
            i = lb
            j = mid + 1
            
            res = []

            while i <= mid and j <= ub:
                
                if arr[i] <= arr[j]:
                    res.append(arr[i])
                    i += 1
                else:
                    res.append(arr[j])
                    j += 1
                    
            while i <= mid:
                res.append(arr[i])
                i += 1
                
            while j <= ub:
                res.append(arr[j])
                j += 1
                
            for idx in range(lb, ub+1):
                arr[idx] = res[idx - lb]
                
        def merge_sort(arr, l, r):
            
            if l < r:
                mid = (l + r) // 2
                
                merge_sort(arr, l, mid)
                merge_sort(arr, mid+1, r)
                merge(arr, l, mid, r)
                
        merge_sort(arr, l, r)
                
            
            
