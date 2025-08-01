#Leetcode - https://leetcode.com/problems/largest-rectangle-in-histogram/description/

#Assume each index element to be smallest and then find max possible area for that histogram
#Then find the previous small element and next small element till those we can expand considering current bar to be smallest amongst considered bars.
#then area will be lenght of interval* height of current bar

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        nse = [n]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        pse = [-1]*n
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                pse[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, (nse[i] - 1 - pse[i])*heights[i])

        return res
