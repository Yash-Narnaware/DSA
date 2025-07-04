#GFG - https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

#same as finding first and last occurences just have to return a different value.

class Solution:
    def countFreq(self, arr, target):
        #code here
        
        n = len(arr)
        l = 0
        r = n - 1

        #first
        while l <= r:
            mid = (l + r) // 2

            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        first = l if l < n and arr[l] == target else -1

        last = -1
        l = 0
        r = n - 1

        #last
        while l <= r:
            mid = (l + r) // 2

            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        last = r if r >= 0 and arr[r] == target else -1

        return last - first + 1 if last != -1 else 0
