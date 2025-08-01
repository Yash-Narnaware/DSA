#GFG - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

#Use merge sort - count inversions during merging 2 sorted arrays. - use the fact that left subarray elements will always come before right sub array elements and for any element if left element > right element then we found pair for all elements from current i pointer till end because array is sorted and later elements will be >= current element.

class Solution:
    def inversionCount(self, arr):

        def merge(a, b, cnt):
            n1 = len(a)
            n2 = len(b)
            
            res = []
            i, j = 0, 0
            
            while i < n1 and j < n2:
                if a[i] > b[j]:
                    cnt[0] += n1 - i
                    res.append(b[j])
                    j += 1
                else:
                    res.append(a[i])
                    i += 1
                    
            while i < n1:
                res.append(a[i])
                i += 1
            
            while j < n2:
                res.append(b[j])
                j += 1
                
            return res
            
        def merge_sort(arr, cnt):
            if len(arr) <= 1:
                return arr
                
            mid = len(arr) // 2
            
            left = merge_sort(arr[:mid], cnt)
            right = merge_sort(arr[mid:], cnt)
            
            return merge(left, right, cnt)
        
        cnt = [0]
        merge_sort(arr, cnt)
        
        return cnt[0]
                
                    
