#Leetcode - https://leetcode.com/problems/next-greater-element-ii/description/

#To simulate circular stucture use % and traverse from 2n - 1 index to 0 but effectve index will be i % n.
#For the later extra n element we just have to maintain the monotonic stack and dont have to calculate/store next greater element.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        n = len(nums)
        res = [-1]*n

        for i in range(2*n - 1, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
                else:
                    res[i] = -1

            stack.append(nums[i%n])

        return res

#Another approach to do the same - just little bit more straightforward

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        n = len(nums)
        res = [-1]*n

        #Just traversing one pass reversed and create monotonic stack order to simulate circular thing.
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            stack.append(nums[i%n])
        
        #now getting next greater element using normal monotonic stack method
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1

            stack.append(nums[i%n])

        return res
        
        
