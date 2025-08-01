#Leetcode - https://leetcode.com/problems/sum-of-subarray-minimums/description/

#calculate next smaller element indices and previous smaller element indices and calculate the subarrays with ith element as minimum and add them up. 
#For ith element the number of subarrays in which theat ith element is minimum is number of elements between pse * number of elements between nse((i - pse[i])*(nse[i] - i))

#Consider edge cases when duplicate elements appear - only consider them in pse or nse and not both. other =wise we are considering some subarrays again and again.

from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(arr)
        nse = [n]*n

        #Calculating the next smaller element index
        stack = deque([])
        for i in range(n-1, -1, -1):
            #To handle edge case(equal elements) we pur <=
            while stack and arr[i] <= stack[-1][0]:
                stack.pop()

            if stack:
                nse[i] = stack[-1][1]
            stack.append((arr[i], i))

        pse = [-1]*n
        #Calculating the previous smaller element index
        stack = deque([])
        for i in range(n):
            while stack and arr[i] < stack[-1][0]:
                stack.pop()

            if stack:
                pse[i] = stack[-1][1]
            stack.append((arr[i], i))

        #calculating number of subarrays with ith element as minimum
        res = 0
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            res += (left*right*arr[i])

        return res % MOD


        
