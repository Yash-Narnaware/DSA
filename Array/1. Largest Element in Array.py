#GFG - https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1

class Solution:
    def largest(self, arr):

        res = arr[0]
        for i in range(1, len(arr)):
            res = max(res, arr[i])
        return res
