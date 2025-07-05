#Leetcode - https://leetcode.com/problems/kth-missing-positive-number/description/

#Using mid and element at mid chek till that point how many +ve integers are missing depending on that shring the arr.
#At the end we will get lowerbound till that element missing integers are < k and after that index it will be > k.

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        n = len(arr)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            no_of_missing = arr[mid] - (mid + 1)

            if no_of_missing >= k:
                r = mid - 1
            else:
                l = mid + 1

        return arr[r] + (k - (arr[r] - (r+1)))
        
