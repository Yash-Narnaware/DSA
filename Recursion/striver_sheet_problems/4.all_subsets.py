#Leetcode - https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        def func(current, n1, res):

            if n1 == n:
                res.append(current[:])
                return

            #include
            current.append(nums[n1])
            func(current, n1 + 1, res)
            current.pop()

            #Exclude
            func(current, n1 + 1, res)

        res = []
        func([], 0, res)

        return res
