#GFG - https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

#Start from right to left and keep track of max element till current element if max element value = current element value then it is a leader because it means we dont have greater element than curret to its right side.

class Solution:
    def leaders(self, arr):

        arr_max = arr[-1]
        res = []
        n = len(arr)
        
        for i in range(n - 1, -1, -1):
            if arr[i] >= arr_max:
                arr_max = arr[i]
            if arr_max == arr[i]:
                res.append(arr[i])
        
        return res[::-1]
