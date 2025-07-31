#Leetcode - https://leetcode.com/problems/next-greater-element-i/submissions/1718891473/

#Very important concept - monotonic stack. - traverse from right to left and for current element till now we have stored elements in stack in decresing order find next greater element in stack till then keep popping elements
#Imagine poles.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res_dict = {}
        stack = []

        n = len(nums2)

        for i in range(n - 1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            
            if not stack:
                res_dict[nums2[i]] = -1
            else:
                res_dict[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        res = []
        for i in nums1:
            res.append(res_dict[i])

        return res

                
  
        
