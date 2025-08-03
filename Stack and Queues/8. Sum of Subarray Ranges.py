#Leetcode - https://leetcode.com/problems/sum-of-subarray-ranges/description/

#didnt understood the intuition behind this approach - calculate sum of subarray minimum and then calculate sum of sub-array maximum then return maximum - minimum.

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        n = len(nums)
        nse = [n]*n

        #Calculating the next smaller element index
        stack = deque([])
        for i in range(n-1, -1, -1):
            while stack and nums[i] <= stack[-1][0]:
                stack.pop()

            if stack:
                nse[i] = stack[-1][1]
            stack.append((nums[i], i))

        pse = [-1]*n
        #Calculating the previous smaller element index
        stack = deque([])
        for i in range(n):
            while stack and nums[i] < stack[-1][0]:
                stack.pop()

            if stack:
                pse[i] = stack[-1][1]
            stack.append((nums[i], i))

        #calculating number of subarrays with ith element as minimum
        res1 = 0
        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            res1 += (left*right*nums[i])


        nge = [n]*n

        #Calculating the next greater element index
        stack = deque([])
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()

            if stack:
                nge[i] = stack[-1][1]
            stack.append((nums[i], i))

        pge = [-1]*n
        #Calculating the previous greater element index
        stack = deque([])
        for i in range(n):
            while stack and nums[i] > stack[-1][0]:
                stack.pop()

            if stack:
                pge[i] = stack[-1][1]
            stack.append((nums[i], i))

        #calculating number of subarrays with ith element as maximum
        res2 = 0
        for i in range(n):
            left = i - pge[i]
            right = nge[i] - i

            res2 += (left*right*nums[i])

        return res2 - res1


        

        

        
        
